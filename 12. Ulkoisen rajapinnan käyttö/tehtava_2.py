import requests
import colorama
from geopy.geocoders import Nominatim
import json

koordinaatin_hakija = Nominatim(user_agent="sää_tiedot")
valinta = input("Syötä paikkakunnan nimi ja paina Enter!:")
valittu_paikka = valinta
avain = "c11b84ccd9a085bb60e6e47615307562"
sijainti = koordinaatin_hakija.geocode(valinta)
lat = sijainti.latitude
lon = sijainti.longitude
units = "metric"
pyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={avain}"
vastaus = requests.get(pyynto).json()
print(vastaus)


print(f"Sijainti: {vastaus['name']}\n"
      f"Sää: {vastaus['weather'][0]['main']}\n"
      f"Lämpötila: {vastaus['main']['temp']}")