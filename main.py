from cgitb import reset
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@bot.command(name='hello', help='Responds with Hi!')
async def hello(ctx):
    # if message.author == client.author:
    #    return

    await ctx.send('Hi!')

client.run(os.getenv('TOKEN'))
