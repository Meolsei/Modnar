import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def age(self, ctx, birth):
        """Gives the user the 18+ role if applicable. Can remove the role if the user already has it.
        The format is YYYY-mm-dd. Example: 2000-12-23"""

        role = ctx.guild.get_role(807955779113451522)
        born = birth
        dob = datetime.datetime.strptime(born, '%Y-%m-%d')
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        if age <18:
            await ctx.send(f"Role cannot be given, your age is {age}.")
        else:
                await ctx.message.author.add_roles(role)
                await ctx.send(f"Role given!")

    @age.error
    async def age_handle(self, ctx, error):
        role = ctx.guild.get_role(807955779113451522)

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Invalid format provided. `YYYY-mm-dd`, or `2004-02-24` for example.")
        elif isinstance(error, commands.MissingRequiredArgument):
            if role in ctx.message.author.roles:
                await ctx.message.author.remove_roles(role)
                await ctx.send("Role removed!")
            else:
                await ctx.send("No date provided. `YYYY-mm-dd`, or `2004-02-24` for example.")
        else:
            raise error

async def setup(bot):
    await bot.add_cog(Misc(bot))