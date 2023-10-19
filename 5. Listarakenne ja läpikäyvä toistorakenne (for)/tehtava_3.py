
while True:

    userinput = input("kirjoita jaettava luku")


    if (any(c.isalpha() for c in userinput) or any(c.isspace() for c in userinput)
          or not any(c.isdigit() for c in userinput)) or len(userinput) <= 0:
        print("vain lukuja")
        continue

    else:
        break

i = int(userinput)
jaollisetKerrat = 0

while i > 0:

    if float(userinput) % i == 0:
        jaollisetKerrat += 1

    i -= 1

if jaollisetKerrat != 2:
    print("Luku ei ole alkuluku")

else:
    print("Luku on alkuluku")


