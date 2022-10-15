import discord
from discord.ext import commands
import aiohttp

class Fun(commands.Cog):
    """Commands that generally are not necessarily important, but are just used anyway for entertainment purposes."""
    
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def cats(self, ctx):
        """Provides a free cat image. *Nya*"""

        url = "https://api.thecatapi.com/v1/images/search"
        api_key = "0969b28f-9159-4dc0-b231-5ab05e22a8ec"

        headers = {"x-api-key": api_key}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                data = await response.json()
                
                embed = discord.Embed(title="Cat!", description="Nyah~")
                embed.set_footer(text="Enjoy your free cat!")
                embed.set_image(url=data[0]['url'])

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))