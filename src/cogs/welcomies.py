import discord 
from discord.ext import commands
class Welcomies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'!Bienvenido {member}¡')
        await ctx.send(f'!Bienvenido {member}¡')    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'!Adiós {member}¡ :(')
        await ctx.send(f'!Adiós {member}¡ :(')
    @commands.Cog.listener()
    async def on_ready(self):    
        print('Nagatoro ha iniciado con exito')     
    
   
def setup(bot):
    bot.add_cog(Welcomies(bot))    