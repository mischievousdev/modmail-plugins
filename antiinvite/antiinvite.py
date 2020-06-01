import re
import discord
from discord.ext import commands

class Antiinvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        match = re.search(r"(?:https?://)?discord(?:(?:app)?\.com/invite|\.gg)/?[a-zA-Z0-9]+/?", message.content)
        if match:
            member = message.guild.get_member(message.author.id) # doing this coz message.author is discord.User, but for checking permissions i need discord.Member
            if member.guild_permissions.manage_server:
                return
            else:
                await message.delete()
                await message.channel.send(f"Deleted a invite link posted by {message.author.mention}")
        else:
            return

def setup(bot):
    bot.add_cog(Antiinvite(bot))