import os
import time
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from youtube_dl import YoutubeDL

load_dotenv()

# Get the API token from the .env file.
DISCORD_TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='^',intents=intents)

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel.")
    bot_voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await bot_voice_channel.connect()
    else:
        await ctx.voice_client.move_to(bot_voice_channel)

@bot.command(name='leave', help='Tells the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play', help='Plays song')
async def play(ctx,*url):
    # TODO: Check to see if it's already in another channel
    # TODO: Needs a check to see if a song is already playing
    # TODO: Create a queue service
    bot_voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await bot_voice_channel.connect()
    else:
        await ctx.voice_client.move_to(bot_voice_channel)
        time.sleep(2)
    
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
        }
    YDL_OPTIONS = {
        'format': "bestaudio/best",
        'default_search': "ytsearch:",
        # 'extractaudio': True,
        # 'audioquality': 0,
        'noplaylist': True
    }

    vc = ctx.voice_client

    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(' '.join(url)) 
        except:
            info = ydl.extract_info(f"ytsearch:{' '.join(url)}", download=False)['entries'][0]
        else:
            info = ydl.extract_info(' '.join(url), download=False)
        url2 = info['entries'][0]['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)

@bot.command(name='pause', help='Pauses song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)