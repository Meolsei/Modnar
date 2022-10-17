import discord
from discord.ext import commands

class Load(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect():
        print("Connected, wait.")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name}#{self.bot.user.discriminator} loaded.")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Contact Meolsei#4905 for issues"))

async def setup(bot):
    await bot.add_cog(Load(bot))