import discord
from discord.ext import commands
import aiohttp
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Information(commands.Cog):
    """Various information."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(aliases=['stat','distat','discordstatus','discord'])
    async def status(self, ctx):
        """Gets Discord's status from https://discordstatus.com/"""

        async with aiohttp.ClientSession() as session:
            async with session.get("https://discordstatus.com/api/v2/summary.json") as response:
                data = await response.json()
                    
                embed = discord.Embed(title="Discord Status:")
                
                try:
                    incidentName = data['incidents'][0]['name']

                except IndexError:
                    incidentName = data['status']['description']
                embed.add_field(name="Incident:", value=incidentName)

                try:
                    incidentImpact = data['incidents'][0]['impact']
                    embed.add_field(name="Impact:", value=incidentImpact)
                except IndexError:
                    incidentImpact = "No incident is ongoing."

                try:
                    incidentStatus = data['incidents'][0]['incident_updates'][0]['status']
                    embed.add_field(name="Status:", value=incidentStatus)
                except IndexError:
                    incidentStatus = "No incident is ongoing."
                    embed.description = "There is no incident ongoing at the moment. If you would like to view past incidents, go to [the status page.](https://discordstatus.com/api/v2/summary.json)"
                

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))