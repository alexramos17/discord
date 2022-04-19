import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv(
    'e555f982ef876529e12c97790dfd11daff5d3ad871cd939226e44363cb46b7ca')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
