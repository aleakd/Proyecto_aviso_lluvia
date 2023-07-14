# proyecto d alerta de lluvia, el programa va enviar un mail alertando de lluvias enlas proximas 18 horas cuando este sea el caso.
#trabajo con la API de: "https://openweathermap.org/"

import requests
import smtplib

my_email = "correo de gmail desde el cual se mandara la alerta"
password = "Password para la app"

key_api = "crear la api key"
dt_tiempo = "https://api.openweathermap.org/data/2.5/forecast"

parametros = {
          "lat": -00.000000,#colocar latitud a consultar
          "lon": -00.000000, #colocar longitud a consultar
          "appid": key_api,
}

dt = requests.get(dt_tiempo,params=parametros)
dt.raise_for_status()


#datos en formato jsno, en una lista, hasta el numero 6
lista_datos = (dt.json()["list"][:6])
print(lista_datos)


llueve = False

for weather in lista_datos:
     id_tiempo = weather["weather"][0]["id"]
     print(id_tiempo)
     if int(id_tiempo) < 700:
          llueve = True

if llueve:
     print("se va a cagar lloviendo")
     with smtplib.SMTP("smtp.gmail.com") as coneccion:
          coneccion.starttls()
          coneccion.login(user=my_email, password=password)
          coneccion.sendmail(from_addr=my_email,
                             to_addrs="casilla a enviar el correo",
                             msg=f"Subjet:Noticia de lluvia\n\n hoy va a llover segun mi app")