# https://stackoverflow.com/questions/53604339/how-do-i-make-my-discord-py-bot-play-mp3-in-voice-channel
print("Iniciando Nagatoro...")
import discord
from discord.ext import commands,tasks
import datetime
from urllib import parse, request
import re
import os
bot = commands.Bot(command_prefix='N ', description="Nagatoro bot")

##BOTS COMMANDS ==========================================================================================================================================================
@bot.command(help = "Comando para programar >:)")
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command(help = "Comando para programar >:)") 
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')    

@bot.command(help = "Comando para programar >:)")
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')   
    bot.load_extension(f'cogs.{extension}')    
#Para que se inicien todos los comandos al iniciar el programa
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
 
@bot.command(name = "Reiniciar: ", aliases = ["r","reiniciar","re",],help = "Reinicia a Nagatoro >:(") 
async def restart(ctx):
    await ctx.send("Reiniciando.")
    await bot.close()   

@bot.listen()
async def on_message(message):
    if "nagatoro" in message.content.lower():
        
        await message.channel.send('¿Estan habalando de mi?')
        await bot.process_commands(message)

bot.run('NzQyMzEzMDQ5MDQ1ODYwMzgz.XzES5g.tR-f38oJo2-I9x_vOWwZjNb-iyM')
