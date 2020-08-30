import discord
from discord.ext import commands

class VoiceLink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, vcid: int):
        if ctx.author.id == 187588641256636416:
            if ctx.voice_client is not None:
                await ctx.voice_client.disconnect()
                vc = self.bot.get_channel(vcid)
                await vc.connect()
                await ctx.send("Done")
            else:
                vc = self.bot.get_channel(vcid)
                await vc.connect()
                await ctx.send("Done")
        else:
            return

    @commands.command()
    async def leave(self, ctx, vcid: int):
        if ctx.author.id == 187588641256636416:
            #vc = self.bot.get_channel(vcid)
            await ctx.voice_client.disconnect()
            await ctx.send("Done")
        else:
            return

def setup(bot):
    bot.add_cog(VoiceLink(bot))
