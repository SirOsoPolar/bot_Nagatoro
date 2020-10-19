#Objetivo, doxxing
class Persona():
    def __init__(self, nombre, busqueda, informacion):
        self.nombre = nombre
        self.busqueda = busqueda
        self.informacion = informacion

    def busqueda_sugerida(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options
        import time

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        palabra_busqueda = self.nombre
        numero_busqueda = self.busqueda + 1
        driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=r"C:\dchrome\chromedriver.exe")

        driver.get("https://www.google.com")
        time.sleep(5)
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys(palabra_busqueda)
        time.sleep(5)
        lista_busquedas_sugeridas = []
        for i in range(1, numero_busqueda):
            elementos = driver.find_element_by_xpath(
                "//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text

            lista_busquedas_sugeridas.append(elementos)
        driver.close()
        return lista_busquedas_sugeridas

    def busqueda_resultados(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options
        import time

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        palabra_busqueda = self.nombre
        numero_busqueda = self.busqueda + 1
        driver = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=r"C:\dchrome\chromedriver.exe")

        driver.get("https://duckduckgo.com/?q=" +
                   str(palabra_busqueda)+"&t=brave&ia=web")
        time.sleep(1)
        busqueda = driver.find_element_by_name("q")
        busqueda.send_keys(palabra_busqueda)
        time.sleep(1)
        lista_busquedas_resultados = []
        for i in range(1, numero_busqueda):
            elementos = driver.find_element_by_xpath(
                "//*[@id='r1-"+str(i)+"']/div/div[1]/div/a").text
            lista_busquedas_resultados.append(elementos)
        driver.close()
        return lista_busquedas_resultados

    def perfiles_facebook(self):
        palabra_busqueda = self.nombre
        palabra_busqueda = palabra_busqueda.replace(' ', '-')
        informacion = self.informacion
        informacion = informacion.replace(' ', '_')
        link_perfiles = ("https://facebook.com/public/" +
                         str(palabra_busqueda)+"_"+str(informacion))
        return link_perfiles


class Facebook():
    def __init__(self, nombre, informacion):
        self.nombre = nombre
        self.informacion = informacion

    def llamada_facebook_nombres(self):
        uno1 = self.nombre.split(' ')
        tres = self.informacion
        for i in uno1:
            persona = Persona(i, tres)
            
            print(persona)
            try:
                for j in uno1:
                    if j == i:
                        print("", end="")
                    else:
                        persona = Persona(i+" "+j, tres)
                        print(persona)
                    try:
                        for k in uno1:
                            if k == j or i == j:
                                print("", end="")
                            else:
                                persona =(i+" "+j+" "+k, tres)
                                
                                print(persona)
                                try:
                                    for l in uno1:
                                        if k == j or i == j or l == k:
                                            print("", end="")
                                        else:
                                            persona = Persona(i+" "+j+" "+k+" "+l, tres)
                                            
                                            print(persona)
                                except Exception:
                                    print("", end="")
                            pass
                    except Exception:
                        print("", end="")
            except Exception:
                print("", end="")

    def llamada_facebook_informacion(self):
        uno1 = self.informacion.split(' ')
        tres = self.nombre

        for i in uno1:
            persona = Persona(uno, i)
            
            print(persona)
            try:
                for j in uno1:
                    if j == i:
                        print("", end="")
                    else:
                        (uno, i+" "+j)
                        

                        print(persona)
                    try:
                        for k in uno1:
                            if k == j or i == j:
                                print("", end="")
                            else:
                                (uno, i+" "+j, " "+k)

                                
                                print(persona)
                                try:
                                    for l in uno1:
                                        if k == j or i == j or l == k:
                                            print("", end="")
                                        else:
                                            (uno, i+" "+j, " "+k+" "+l)
                                            print(persona)
                                except Exception:
                                    print("", end="")
                    except Exception:
                        print("", end="")
            except Exception:
                print("", end="")

def perfiles_facebook(nombre,informacion):

    palabra_busqueda = nombre
    palabra_busqueda = palabra_busqueda.replace(' ', '-')
    informacion = informacion
    informacion = informacion.replace(' ', '_')
    link_perfiles = ("https://facebook.com/public/" +
                     str(palabra_busqueda)+"_"+str(informacion))
    return link_perfiles

def delimitador_facebook(nombre, palabras):
    persona = Facebook(nombre, palabras)
    lista1 = persona.llamada_facebook_nombres()
    print(lista1)
    lista2 = persona.llamada_facebook_informacion()
    print(lista2)


#delimitador_facebook("Hugo Andres", "Durango")
perfiles_facebook("Hugo","Durango")

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


def hablar_bot():
    import pyttsx3 as habla
    import pyautogui as gui
    import time

    Nagatoro = habla.init()
    # help(Nagatoro)
    voces = Nagatoro.getProperty('voices')
    Nagatoro.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Nagatoro.setProperty('rate', 120)
    Nagatoro.save_to_file('El arzobispo de constantinopla,se quiere desarzobispoconstantinopolitanizar,el desarzobispadorconstantinapolitanizadorque lo desarzobispoconstantinopolitanice,buen desarzobispadorconstantinapolitanizador será.', 'NagatoroDice.mp3')
    Nagatoro.runAndWait()


def eliminar_voz():
    import os
    os.system('del C:/Users/Hugo/Desktop/Nagatoro-Bot/NagatoroDice.mp3')


algo = Persona("N", 2, "N")
xd = algo.busqueda_resultados()
print(xd)
