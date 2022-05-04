import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import music

cogs = [music]

load_dotenv()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Dicord!')


@client.command(name='hello', help='Responds with Hi!')
async def hello(ctx):
    await ctx.send("Hi!")

client.run(os.getenv('TOKEN'))
