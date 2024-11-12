###############################################################################
# Copyright (C) 2024 Romuald, FRS077 <fra485@orange.fr>  
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
###############################################################################


import requests  
from gtts import gTTS

# Remplacez 'your_api_key' par votre clé API OpenWeatherMap  
API_KEY = '77d9ca3addc1f112c2d8663ea07f1393'
CITY = 'Lille'  # Changez cela pour la ville que vous voulez  
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Récupérer la météo  
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    # Extraire les informations météo  
    temperature = data['main']['temp']  # Température en degrés Celsius  
    wind_speed = data['wind']['speed']   # Vitesse du vent en m/s  
    wind_deg = data['wind']['deg']       # Direction du vent en degrés  
    humidity = data['main']['humidity']   # Humidité en pourcentage  
    rain_amount = data.get('rain', {}).get('1h', 0)  # Précipitations en mm pour la dernière heure

    # Convertir la direction du vent en cardinal (N, NE, E, SE, S, SW, W, NW)
    if 337.5 <= wind_deg < 360 or 0 <= wind_deg < 22.5:
        wind_direction = "Nord"
    elif 22.5 <= wind_deg < 67.5:
        wind_direction = "Est-Nord-Est"
    elif 67.5 <= wind_deg < 112.5:
        wind_direction = "Est"
    elif 112.5 <= wind_deg < 157.5:
        wind_direction = "Est-Sud-Est"
    elif 157.5 <= wind_deg < 202.5:
        wind_direction = "Sud"
    elif 202.5 <= wind_deg < 247.5:
        wind_direction = "Ouest-Sud-Ouest"
    elif 247.5 <= wind_deg < 292.5:
        wind_direction = "Ouest"
    elif 292.5 <= wind_deg < 337.5:
        wind_direction = "Ouest-Nord-Ouest"

    # Préparer l'information météo  
    weather_info = (
        f"Voici le bulletin météo."
        f"La température à {CITY} est de {temperature} degrés.\n"
        f"La vitesse du vent est de {wind_speed} mètres par seconde venant de {wind_direction}.\n"
        f"L'humidité est de {humidity} %.\n"
        f"Les précipitations de pluie dans les dernières heure sont de {rain_amount} millimètres."

    )

    # Sauvegarder les informations dans un fichier texte  
    with open("meteo.txt", "w") as text_file:
        text_file.write(weather_info)

    # Convertir le texte en audio  
    tts = gTTS(text=weather_info, lang='fr')
    tts.save("meteo.wav")

    print("Météo enregistrée dans 'meteo.txt' et convertie en 'meteo.wav'.")
else:
    print("Erreur lors de la récupération des données météo:", data.get("message", "Erreur inconnue"))
