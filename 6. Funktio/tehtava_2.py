import random


def noppa(tahkomaara):
    return random.randint(1, tahkomaara)

userInput = input("Kerro nopan tahkojen määrä:")
heittoKerrat = 0

print(f"Heitän noppaa kunnes tulee maksimiluku:{userInput}")

while True:
    silmäluku = noppa(int(userInput))
    print(silmäluku)
    heittoKerrat += 1

    if silmäluku == int(userInput):
        break

print(f"Noppaa heitettiin: {heittoKerrat} kertaa!")
