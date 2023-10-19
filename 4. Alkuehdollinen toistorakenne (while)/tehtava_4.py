import random

randomNum = random.randint(1,10)

while True:

    userInput = input("Arvaa numero 1-10")

    if (any(c.isalpha() for c in userInput) or any(c.isspace() for c in userInput)
        or not any(c.isdigit() for c in userInput) or len(userInput) == 0):
        print("Vain luvut 1-10!")
        continue

    elif int(userInput) < randomNum:
        print("Liian pieni arvaus")
        continue

    elif int(userInput) > randomNum:
        print("Liian suuri arvaus")
        continue

    elif int(userInput) == randomNum:
        print("Oikein")
        break

