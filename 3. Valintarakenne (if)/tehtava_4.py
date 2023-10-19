def karkausvuosi_laskin (vuosiluku):
    vaihtoehto_a = float(vuosiluku % 4)
    vaihtoehto_b = float(vuosiluku % 100)
    vaihtoehto_c = float(vuosiluku % 400)

    if vaihtoehto_a == 0 and vaihtoehto_b > 0:
        print("vuosi on karkausvuosi!")

    elif vaihtoehto_c == 0:
        print("vuosi on karkausvuosi!")

    else:
        print("vuosi ei ole karkausvuosi!")


vuosiluku = 0

i = 0

while i < 1:
    userinput = input("Kerro vuosiluku:")

    if userinput.isdigit():
        vuosiluku = int(userinput)
        i += 1

karkausvuosi_laskin(vuosiluku)