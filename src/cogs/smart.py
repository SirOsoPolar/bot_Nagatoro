import discord 
from discord.ext import commands
import random

class Smart(commands.Cog):


    
    def __init__(self, bot):
        self.bot = bot
        self.diccionario_keys = {"Hola":{1:{3:"Buenas noches"},2:{5:"Funciono >*"}}}
        self.diccionario_respuestas= {}
        self.diccionario_suerte = {}
        self.old_message = ""
        self.boca = True
    
    
    @commands.command(name = "Chat:", aliases = ["chat","cjat","mensajes","escribe"],help = "Nagatoro escribe en el chat lo que hara que ponga lo que ha aprendido")
    async def escribe(self,ctx):
        self.boca = True 
        await ctx.send(f'el estatus de chat es:  {round(boca)}.') 

    @commands.command(name = "Callate:", aliases = ["calla","silencio","shh"],help = "Nagatoro no escribira en el chat, pero seguira aprendiendo")
    async def silencio(self,ctx):
        self.boca = False
        await ctx.send(f'el estatus de chat es:  {round(boca)}.')

    @commands.Cog.listener()
    async def on_message(self,message,):
        if self.boca == True:
            if "prueba" in message.content.lower():
                await message.channel.send('Charla de testeo')
                await self.bot.process_commands(message)
            mensaje_str = message.content
            mensaje_ar = message.content.split(' ')
            if (message.author.bot):
                print("un bot escribio este mensaje")
            else:    
                if mensaje_str in self.diccionario_keys.keys():
                    dic_res = self.diccionario_keys[mensaje_str]
                    karma = 0
                    lista_karma = []
            
                    for i in range(1,len(dic_res)+1):
                        dic_suer = dic_res[i]
                        suma = sum(dic_suer.keys())
                        karma = karma + suma
                        lista_karma.append(suma)
                    i = 0
                    ganador = 0
                    while i == 0:
                        probabilidad = 100+karma//karma
                        for j in lista_karma:
                            intentos = j*probabilidad
                            for k in range(1,intentos):
                                numero_random = random.randint(1,100+karma)
                                if numero_random == j:
                                    ganador = j
                                    i = 2
                    for i in range(1,len(dic_res)+1):
                        dic_suer=dic_res[i]
                        if ganador in dic_suer.keys():
                            await message.channel.send(dic_suer[ganador])
                            pass    

                    self.diccionario_keys[self.old_message]={}        
                    dic_res=self.diccionario_keys[self.old_message]
                    dic_suer={1:f"{mensaje_str}"}
                    dic_res[len(dic_res)+1]=dic_suer        

                else:
                    len_dic_res = len(self.diccionario_respuestas)
                    self.diccionario_suerte[1]=message.content
                    self.diccionario_respuestas[1]=self.diccionario_suerte
                    self.diccionario_keys[self.old_message]=self.diccionario_respuestas
                    self.old_message= message.content

def setup(bot):
    bot.add_cog(Smart(bot))    