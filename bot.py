import os
import discord
from dotenv import load_dotenv
from game import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
game = Game()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!init'):

        try:
            game.init_game()
            game.print_board()
            embed = discord.Embed(
                title=f"{message.author}'s Minesweeper game",
                color=discord.Color.light_gray()
            )
            embed.add_field(name="Tiles", value=str(game.tiles), inline=True)
            embed.add_field(name="Turns", value=str(1), inline=True)
            embed.add_field(name="", value=game.board_str, inline=False)

            await message.channel.send(embed=embed)
        except:
            await message.channel.send(f"Error. `game.board.str` is {len(game.board_str)} characters long.")
            
        return

client.run(TOKEN)