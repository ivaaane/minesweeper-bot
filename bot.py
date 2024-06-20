import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from game import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)
game = Game()
color = discord.Color.light_gray()

# -- Bot commands --

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.tree.sync()
    
def game_loop(author): # This sends the embed message to Discord
    game.print_board()
    embed = discord.Embed(title=f"{author.display_name}'s Minesweeper game", color=color)
    embed.add_field(name="Tiles", value=str(game.tiles), inline=True)
    embed.add_field(name="Turns", value=str(game.turns), inline=True)
    embed.add_field(name="", value=game.board_str, inline=False)
    return embed

# Start game
@bot.tree.command(name="start", description="Start a new Minesweeper game.")
async def init(interaction:discord.Interaction):
    if not game.active:
        game.init_stats()
        await interaction.response.send_message(embed=game_loop(interaction.user)) 
    else:
        await interaction.response.send_message(embed=
                discord.Embed(description=f"A game by {interaction.user.display_name} has already started!", color=color))
        
# Continue game
@bot.tree.command(name="r", description="Reveal a tile from the board.")
async def reveal(interaction:discord.Interaction, row:str, column:int):
    if game.active:
        if game.reveal_tile(row, column):
            await interaction.response.send_message(embed=game_loop(interaction.user))
        else:
            await interaction.response.send_message(embed=
                    discord.Embed(description="There was an error with the command syntax.", color=color))
    else:
        await interaction.response.send_message(embed=
                    discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))
        
# Place flag
@bot.tree.command(name="f", description="Place a flag in the board.")
async def reveal(interaction:discord.Interaction, row:str, column:int):
    if game.active:
        if game.place_flag(row, column):
            await interaction.response.send_message(embed=game_loop(interaction.user))
        else:
            await interaction.response.send_message(embed=
                    discord.Embed(description="There was an error with the command syntax.", color=color))
    else:
        await interaction.response.send_message(embed=
                    discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))
        
# Help
@bot.tree.command(name="help", description="Learn how to play.")
async def reveal(interaction:discord.Interaction):
    await interaction.response.send_message(embed=
    discord.Embed(description="I have to write this later dfgbhjki", color=color))

# End game
@bot.tree.command(name="cancel", description="Cancel your current Minesweeper game.")
async def init(interaction:discord.Interaction):
    if game.active:
        game.active = False
        await interaction.response.send_message(embed=
                discord.Embed(description=f"{interaction.user.display_name}'s game was cancelled.", color=color)) 
    else:
        await interaction.response.send_message(embed=
                discord.Embed(description=f"There's no game active for {interaction.user.display_name}.", color=color))

bot.run(TOKEN)