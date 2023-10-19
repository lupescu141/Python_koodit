import requests
import colorama

pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto).json()
print(f"{colorama.Fore.LIGHTYELLOW_EX}{vastaus['value']}{colorama.Style.RESET_ALL}")
