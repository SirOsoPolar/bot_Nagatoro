import discord 
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
class Navigator_Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "Busqueda por navegador:", aliases = ["google","navegar","buscar","search","s"],help = "Nagatoro usa el navegador para buscar tu palabra")
    async def search(self,ctx,nombre:str,busqueda:int):
        name = nombre
        search = busqueda
        try:
            if search>0 and search<=10:            
                await ctx.send("Me tomare mi tiempo en buscar eso...")
                persona = Persona(name,busqueda)
                time.sleep(1)
                lista = persona.busqueda_sugerida()
                await ctx.send(f'Encontre estas {search} busquedas populares:')
                await ctx.send(lista)
                lista2 = persona.busqueda_resultados()
                await ctx.send(f'Encontre estas {search} paginas')
                await ctx.send(lista2)
            else:
                await ctx.send(f'¿Crees que puedo buscar {search}? introduce un valor menor a 10...')          
        except Exception as e:
            print("ocurrio el error ",e)
            await ctx.send(f"{name} parece no ser muy famoso ¿Qué te parece disminuir el numero de busquedas?")
def setup(bot):
    bot.add_cog(Navigator_Search(bot))        


class Persona():
    def __init__(self,nombre,busqueda):
        self.nombre = nombre
        self.busqueda = busqueda 

    def busqueda_sugerida(self):
        
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        palabra_busqueda = self.nombre
        numero_busqueda = self.busqueda + 1
        driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\dchrome\chromedriver.exe")
        
        driver.get("https://www.google.com")
        time.sleep(5)
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys(palabra_busqueda)
        time.sleep(5)
        lista_busquedas_sugeridas=[]     
        for i in range(1,numero_busqueda):
            elementos = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
            lista_busquedas_sugeridas.append(elementos)        
        driver.close()                    
        return lista_busquedas_sugeridas                      

    def busqueda_resultados(self):
    
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        palabra_busqueda = self.nombre
        numero_busqueda = self.busqueda +1
        driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\dchrome\chromedriver.exe")
        
        driver.get("https://duckduckgo.com/?q="+str(palabra_busqueda)+"&t=brave&ia=web")
        time.sleep(5)
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys(palabra_busqueda)
        time.sleep(5)
        lista_busquedas_resultados=[]     
        for i in range(1,numero_busqueda):
            elementos = driver.find_element_by_xpath("//*[@id='r1-"+str(i)+"']/div/div[1]/div/a").text
            lista_busquedas_resultados.append(elementos)                                      
        driver.close()
        return lista_busquedas_resultados

