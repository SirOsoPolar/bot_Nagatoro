import discord 
from discord.ext import commands
class Change_Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True,name = "Entrar:", aliases = ["entrar","join"],help = "Nagatoro entra al canal de la persona que manda el comando")
    async def entrar(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
       
    @commands.command(pass_context=True,name = "Salir:", aliases = ["salir","leave"],help = "Nagatoro sale del canal en el que se encuentra")
    async def salir(self,ctx):
        server = ctx.voice_client
        await server.disconnect()
def setup(bot):
    bot.add_cog(Change_Channel(bot))    