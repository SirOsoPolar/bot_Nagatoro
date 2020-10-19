import discord 
from discord.ext import commands
import time
import pyttsx3 as habla
import pyautogui as gui
import random
class Speak(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['speak',"di","habla"],name="Hablar: ",help="Nagatoro entra al chat de voz y se pone a hablar")
    async def speak(self,ctx,algo:str):
        print(algo)
        algo1 = algo
        print(algo1)
        try :    
            channel = ctx.author.voice.channel
            await channel.connect()
            hablar_bot(algo1)
            guild = ctx.guild
            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            audio_source = discord.FFmpegPCMAudio('NagatoroDice.mp3')       
            
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)
        except Exception as e:
            hablar_bot(algo1)
            guild = ctx.guild
            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            audio_source = discord.FFmpegPCMAudio('NagatoroDice.mp3')  
            
            
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)
            #print(e)   
            #await  ctx.send('¿eehhh?, al parecer no puedo entrar al chat de voz')         
def setup(bot):
    bot.add_cog(Speak(bot))    






def escuchar_bot():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            print("What did you say: {}".format(text))
        except:
            print("I am sorry! I can not understand!")
# escuchar_bot()


def hablar_bot(algo):
    voice = algo
    Nagatoro = habla.init()
    # help(Nagatoro)
    voces = Nagatoro.getProperty('voices')
    Nagatoro.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
        # TTS_MS_EN-US_ZIRA_11.0  # Ingles
        # TTS_MS_ES-MX_SABINA_11.0
    Nagatoro.setProperty('rate', 120)
    
    Nagatoro.save_to_file(f'{voice}', 'NagatoroDice.mp3')
    Nagatoro.runAndWait()


def eliminar_voz():
    import os
    os.remove('C:/Users/Hugo/Desktop/Nagatoro-Bot/src/NagatoroDice.mp3')