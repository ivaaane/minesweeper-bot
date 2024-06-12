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
active = False

# -- Bot Actions --
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    global active
    
    def game_loop(): # This sends the embed message to Discord
        game.print_board()
        embed = discord.Embed(title=f"{message.author}'s Minesweeper game", color=discord.Color.light_gray())
        embed.add_field(name="Tiles", value=str(game.tiles), inline=True)
        embed.add_field(name="Turns", value=str(game.turns), inline=True)
        embed.add_field(name="", value=game.board_str, inline=False)
        return embed
    
    if message.author == client.user:
        return
    if not active:
        # Start game
        if message.content == ('!ms init'):
            active = True
            await message.channel.send(embed=game_loop()) 
            return
        
    else:
        # Continue game
        if message.content.startswith('!'):
            answer = message.content[1:]
            if game.reveal_tile(answer[0],answer[1],answer[2]):
                await message.channel.send(embed=game_loop())

client.run(TOKEN)