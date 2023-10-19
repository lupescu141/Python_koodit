
while True:
    tuumaa = input("Ilmoita tuumien määrä:")

    if any(c.isalpha() for c in tuumaa) or any(c.isspace() for c in tuumaa):
        print("Kirjoita vainn numeroita")
        continue

    elif len(tuumaa) <= 0:
        break

    else:
        print(f"{tuumaa} tuumaa = {float(tuumaa) * 2.54 :.2f} senttimetriä")


