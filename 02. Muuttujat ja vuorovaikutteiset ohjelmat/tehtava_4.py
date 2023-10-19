import math

sanaLista = ["ensimmäinen", "toinen", "kolmas"]
numeroLista = []

i = 0
while i < 3:
    userInput = input(sanaLista[i] + " numero:")

    if any(c.isalpha() for c in userInput) or (len(userInput) == 0):
        print("Kirjoita kokonaisluku!")

    else:
        numeroLista.append(math.floor(float(userInput)))
        i += 1

for x in numeroLista:
    print(x)

print("Lukujen summa: " + str(numeroLista[0] + numeroLista[1] + numeroLista[2]))
print("Lukujen tulo: " + str(numeroLista[0] * numeroLista[1] * numeroLista[2]))
print("Lukujen keskiarvo: " + str(numeroLista[0] + numeroLista[1] + numeroLista[2] / 3))
