# hyödynsin omaa koodiani moduulista 4 tehtävä 3 sopi aivan mainiosti tähän.

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
        numerolista.append(int(userinput))

numerolista.sort(reverse=True)

print(numerolista[0:5])