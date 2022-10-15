#Imports
import os
import os
from aiohttp import ClientConnectorError, ClientResponseError
import discord
from discord.ext import commands
import sys
import asyncio
import time

#Bot Config
intents = discord.Intents(messages=True, guilds=True)
intents.typing = True
intents.presences = True
bot = commands.Bot(commands.when_mentioned_or('>'), owners=['769723790078640168'], status=discord.Status.idle, help_command=None, intents = intents)

#Cogs
path="./cogs"
print("Loading cogs...")
for file in os.listdir(path):
    if file.endswith(".py"):
        l = len(file)
        bot.load_extension(f'cogs.{file[:l-3]}')
        print(f"Loaded cogs.{file[:l-3]}.")


#Events
@bot.event
async def on_connect():
    print("Connected, wait.")

@bot.event
async def on_ready():
    print(f"{bot.user.name}#{bot.user.discriminator} loaded.")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Black Ops 2"))

    
@bot.command(aliases = ['ping', 'ms'])
async def latency(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await asyncio.sleep(2.5)
        await ctx.send(f"Latency: `{ping} ms`.")
    
try:
    bot.run('OTQ5ODgwMTE4MjI5MjE3Mjgw.YiQyzA.Ly4VlItHYGD21CsboC_na_ilBxg')
except ClientConnectorError or ClientResponseError:
    print("Unable to connect to Discord...\nMae, please let me show information...")
    sys.exit()