numerolista = []

while True:

    userinput = input("Syötä lukuja")

    if len(userinput) <= 0:
        break

    elif (any(c.isalpha() for c in userinput) or any(c.isspace() for c in userinput)
          or not any(c.isdigit() for c in userinput)):
        print("vain lukuja")
        continue

    else:
        numerolista.append(float(userinput))

print(f"Pienin luku: {min(float(s) for s in numerolista) :.2f}")
print(f"Suurin luku: {max(float(s) for s in numerolista) :.2f}")
