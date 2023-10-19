import  random

tulos = 0
userInput = input("Montako noppaa heitetään?")

for x in range(int(userInput)):

    tulos += random.randint(1,6)

print(f"Noppien yhteinen pistemäärä: {tulos}")