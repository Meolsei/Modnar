import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def age(self, ctx, *args, **kwargs):
        def check(message):
            return message.author == ctx.author

        role = ctx.guild.get_role(807955779113451522)
        today = datetime.date.today()

        if role not in ctx.author.roles:
            await ctx.reply("Firstly, send the year of birth. Do not execute the command while doing so.")
            message = await self.bot.wait_for("message", check=check)
            if isinstance(int(message.content), int):
                year = message.content
            else:
                return CommandInvokeError

            await ctx.reply("Now, send the birth month. Use the number, not the name.")
            message = await self.bot.wait_for("message", check=check)
            if isinstance(int(message.content), int):
                month = message.content
            else:
                return CommandInvokeError

            await ctx.reply("Lastly, send your birth day. After that, I'll do the rest of the work.")
            message = await self.bot.wait_for("message", check=check)
            if isinstance(int(message.content), int):
                day = message.content
            else:
                return CommandInvokeError

            birth = (f"{year}-{month}-{day}")
            dob = datetime.datetime.strptime(birth, '%Y-%m-%d')
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            await ctx.reply(f"Your age is {age}, right? Please type \"Yes\" or \"No.\"")
            message = await self.bot.wait_for("message", check=check)
            if message.content == "Yes" or "yes":
                await ctx.reply("Okay, giving you the role.")
                await message.author.add_roles(role)
            elif message.content == "No" or "no":
                await ctx.reply("Okay, please rerun the command then.")
        else:
            await ctx.reply("You already have the role, would you like to remove it? Please type \"Yes\" or \"No.\"")
            message = await self.bot.wait_for("message", check=check)
            if message.content == "Yes" or "yes":
                await ctx.reply("Okay, removing the role.")
                await message.author.remove_roles(role)
            elif message.content == "No" or "no":
                await ctx.reply("Okay, have a good day then.")

    @age.error
    async def age_handle(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.reply("Invalid response, please rerun the command.")
        else:
            raise error
                

async def setup(bot):
    await bot.add_cog(Misc(bot))