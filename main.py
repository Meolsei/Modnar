import os
import discord
from discord.ext import commands
import sys

intents = discord.Intents.all()
bot = commands.Bot(commands.when_mentioned_or('>'), owners=['769723790078640168'], status=discord.Status.idle, help_command=None, intents = intents)

async def loadExt():
    print("Loading all available cogs...")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog ({filename})")
        else:
            skipped = []
            skipped.append(filename)
            print(f"{len(skipped)} file(s) skipped.")

@bot.event
async def on_connect():
    await loadExt()
    
try:
    bot.run('OTQ5ODgwMTE4MjI5MjE3Mjgw.GYuSoD.Omre515X2pT7cx4_i_wvhVFv06OupgBka9rZuk')
except ClientConnectorError or ClientResponseError:
    print("Unable to connect to Discord...\nMae, please let me show information...")
    sys.exit()