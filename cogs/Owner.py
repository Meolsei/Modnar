import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ms', 'ping'])
    @commands.is_owner()
    async def latency(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"Latency: `{ping} ms`.")

async def setup(bot):
    await bot.add_cog(Owner(bot))