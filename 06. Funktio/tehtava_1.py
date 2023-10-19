import random


def noppa():
    return random.randint(1,6)


print("Heitän noppaa kunnes tulee silmäluku: 6")

while True:
    silmäluku = noppa()
    print(silmäluku)

    if silmäluku == 6:
        break
