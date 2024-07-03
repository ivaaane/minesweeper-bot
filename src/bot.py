import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from game import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)
games = {}
color = discord.Color.light_gray()

# -- Bot commands --

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.tree.sync()
    
def game_loop(author, game):  # This sends the embed message to Discord
    game.print_board()
    embed = discord.Embed(color=color)
    embed.set_author(name=f"{author.name}", icon_url=f"{author.avatar}")
    embed.add_field(name="Tiles", value=str(game.tiles), inline=True)
    embed.add_field(name="Turns", value=str(game.turns), inline=True)
    embed.add_field(name="", value=game.board_str, inline=False)
    return embed

# Start game
@bot.tree.command(name="start", description="Start a new Minesweeper game.")
async def init(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id not in games or not games[user_id].active:
        games[user_id] = Game()
        games[user_id].init_stats()
        await interaction.response.send_message(embed=game_loop(interaction.user, games[user_id])) 
    else:
        await interaction.response.send_message(embed=
                discord.Embed(description=f"A game by {interaction.user.display_name} has already started!", color=color))
        
# Continue game
@bot.tree.command(name="r", description="Reveal a tile from the board.")
async def reveal(interaction: discord.Interaction, row: str, column: int):
    user_id = interaction.user.id
    if user_id in games and games[user_id].active:
        game = games[user_id]
        if game.reveal_tile(row, column):
            await interaction.response.send_message(embed=game_loop(interaction.user, game))
            if not game.active:
                await interaction.channel.send(embed=
                        discord.Embed(description=f"{interaction.user.display_name}, you lost!", color=color))
            elif game.tiles == 0:
                await interaction.channel.send(embed=
                        discord.Embed(description=f"{interaction.user.display_name}, YOU WON!!!", color=color))
                game.active = False
        else:
            await interaction.response.send_message(embed=
                    discord.Embed(description="There was an error with the command syntax.", color=color))
    else:
        await interaction.response.send_message(embed=
                    discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))
        
# Place flag
@bot.tree.command(name="f", description="Place a flag on the board.")
async def place_flag(interaction: discord.Interaction, row: str, column: int):
    user_id = interaction.user.id
    if user_id in games and games[user_id].active:
        game = games[user_id]
        if game.place_flag(row, column):
            await interaction.response.send_message(embed=game_loop(interaction.user, game))
        else:
            await interaction.response.send_message(embed=
                    discord.Embed(description="There was an error with the command syntax.", color=color))
    else:
        await interaction.response.send_message(embed=
                    discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))
        
# Help
@bot.tree.command(name="help", description="Learn how to play.")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
    embed=discord.Embed(description="""
    # Welcome to Minesweeper Bot!
    
    **Note:** The provided instructions will teach you how to interact with this bot. If you don't know how to play vanilla Minesweeper, I recommend [this article](https://minesweepergame.com/strategy/how-to-play-minesweeper.php).                   
    
    * Start a new game with the `/start` command. The GUI is composed of the board, displayed with emojis, the left tiles counter, the turn counter, and the name of the user.
    * Reveal cells with `/r <row> <column>`. You'll need to provide the coordinates of your cell: they're displayed in the border of the board, the rows being represented with letters and columns with numbers. For example, `/r a 0` will reveal the cell in the top left side.
    * Your first reveal will always be in an empty cell for safety.
    * Same as `/r`, you can place flags with `/f <row> <column>`. Tip: if a number cell has as many flags around its 8 touching cells as the number displays, you can *reveal the number cell* to automatically reveal the remaining cells.
    * The game advances one turn after each action. If you win or lose, a notification will display.
    * You can always cancel your game with `/cancel`.

    *Do you like this project and want to help make it better? Contribute on [GitHub](https://github.com/ivaaane/minesweeper-bot)!*
    
    """, color=color))

# End game
@bot.tree.command(name="cancel", description="Cancel your current Minesweeper game.")
async def cancel(interaction: discord.Interaction):
    user_id = interaction.user.id
    if user_id in games and games[user_id].active:
        games[user_id].active = False
        await interaction.response.send_message(embed=
                discord.Embed(description=f"{interaction.user.display_name}'s game was cancelled.", color=color)) 
    else:
        await interaction.response.send_message(embed=
                discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))

bot.run(TOKEN)
