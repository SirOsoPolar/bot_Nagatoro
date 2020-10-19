import discord 
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Moderacion iniciada con exito")
    @commands.command(name="Limpieza: ",aliases=["limpiar","lim","clear","cls"],help="Nagatoro toma la escoba y barre el chat")
    async def clear(self,ctx,amount:int):
        await ctx.channel.purge(limit= amount)
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Por favor escriba todos los argumentos")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("especifica la cantiadad")
   



def setup(bot):
    bot.add_cog(Moderation(bot))    
