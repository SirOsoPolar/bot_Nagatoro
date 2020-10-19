import discord 
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Nagatorio ha iniciado con exito desde COG')
    #Commands        
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(bot.latency*1000)}ms')
def setup(bot):
    bot.add_cog(Example(bot))    

    
        