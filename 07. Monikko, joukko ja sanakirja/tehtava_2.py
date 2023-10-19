nimia = set()

while True:
    user_input = input("Syötä nimi:")

    if user_input.strip() == '':
        break

    elif nimia.__contains__(user_input):
        print("Aiemmin syötetty nimi")

    else:
        print("Uusi nimi")
        nimia.add(user_input)

for x in nimia:
    print(x)