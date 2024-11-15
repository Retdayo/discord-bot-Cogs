import discord
from discord.ext import commands

# コマンドの定義
class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping')
    async def ping(self, ctx):
        # コマンドが呼ばれた際に、Pong! と返信する
        await ctx.send('Pong!')

# Cogをボットに追加する
def setup(bot):
    bot.add_cog(PingCommand(bot))
