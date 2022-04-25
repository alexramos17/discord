import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl

load_dotenv()

# client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Dicord!')

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         await message.channel.send("Hi!")


@bot.command(name='hello', help='Responds with Hi!')
async def hello(ctx):
    await ctx.send("Hi!")

# client.run(os.getenv('TOKEN'))

bot.run(os.getenv('TOKEN'))
