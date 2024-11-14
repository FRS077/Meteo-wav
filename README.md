# Mettre à jour la liste des paquets
**sudo apt-get update**

# Installer les bibliothèques nécessaires

Installer FFMPEG (Linux)
L’installation sous Linux est relativement simple et peut s’effectuer de différentes manières.
Sur Debian et dérivés
Le paquet ffmpeg est disponible sur les dépôts officiels et cela rend l’installation vraiment aisée il
faut bien le dire !
# Installe ffmpeg
**sudo apt-get install ffmpeg**

# Installe les codecs "classiques" comme mpeg4
**sudo apt-get install libavcodec-unstripped-52 libavdevice-unstripped-52**

# Assurez-vous d'avoir installé requests et gTTS :

**sudo pip install requests gTTS**

**pip install gTTS requests**

**pip install pydub**

**pip install DateTime**

**cd /opt**

**sudo git clone https://github.com/FRS077/Meteo-wav.git**

**cd /Meteo-wav**

# configuration : 
**sudo nano meteo-wav.py**

    Remplacez your_api_key par votre propre clé API que vous obtenez en vous inscrivant sur le site d'OpenWeatherMap.
    Exécutez le script dans votre environnement Python.

Explication des éléments du code

    Récupération des données : Le script utilise l'API OpenWeatherMap pour récupérer les informations météorologiques.
    Traitement des données : Les informations telles que la température, la vitesse et la direction du vent, l'humidité, les précipitations, le lever et le coucher du soleil sont extraites.
    Conversion du texte en audio : Le texte est converti en audio WAV à l'aide de gTTS.
    Modification des caractéristiques audio : Le fichier WAV est ensuite traité avec pydub pour le convertir en 8000 Hz, 16 bits et mono.
    Enregistrement dans un fichier texte : Les informations sont également enregistrées dans un fichier texte pour consultation ultérieure.

Ce script permet d'obtenir toutes les informations météorologiques souhaitées et de les enregistrer de manière appropriée.

