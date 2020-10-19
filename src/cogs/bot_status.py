import discord 
from discord.ext import commands

class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "Ausente:", aliases = ["ausente","au","idle"],help = "Cambia el estado de Nagatoro a ausente")
    async def idle(self,ctx):
        await self.bot.change_presence(status=discord.Status.idle)

    @commands.command(name = "Invisible:", aliases = ["invisible","inv"],help = "Cambia el estado de Nagatoro a invisible")
    async def inv(self,ctx):
        await self.bot.change_presence(status=discord.Status.invisible)

    @commands.command(name = "Desconectado:", aliases = ["desconectar","desc","desconectado","off","offline"],help = "Cambia el estado de Nagatoro a desconectado")
    async def offline(self,ctx):
        await self.bot.change_presence(status=discord.Status.offline)

    @commands.command(name = "En linea:", aliases = ["en linea","on","despierta","online"],help = "Cambia el estado de Nagatoro a ausente")
    async def online(self,ctx):
        await self.bot.change_presence(status=discord.Status.online)

    @commands.command(name = "No molestar:", aliases = ["no molestar","ocupada","nomo","dnd"],help = "Cambia el estado de Nagatoro a no molestar")
    async def dnd(self,ctx):
        await self.bot.change_presence(status=discord.Status.do_not_disturb)    
    @commands.command(name = "En directo:", aliases = ["twitch","tw","rec","stream","directo","dire"],help = "Cambia el estado de Nagatoro a stream o directo")
    async def directo(self, ctx, juego, name):
        await self.bot.change_presence(activity=discord.Streaming(name=juego, url="http://www.twitch.tv/"+name))
        print('My Ready is Body')        



def setup(bot):
    bot.add_cog(Status(bot))   

