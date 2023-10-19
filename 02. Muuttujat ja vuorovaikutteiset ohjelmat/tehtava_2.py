ympyranSade = input('Kirjoita ympyrän säde: ')

while any(c.isalpha() for c in ympyranSade):
    print("Kirjoita vain numeroita!")
    ympyranSade = input('Kirjoita ympyrän säde: ')

ympyranPintaAla = float(ympyranSade) ** 2 * 3.14
print("Ympyrän pinta-ala on: ", ympyranPintaAla)
