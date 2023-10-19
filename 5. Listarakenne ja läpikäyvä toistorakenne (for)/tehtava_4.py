kaupunkiLista = []
mones = ["1/5", "2/5", "3/5", "4/5", "5/5"]
index = 0

for x in range(5):
    kaupunkiLista.append(input(f"Kirjoita kaupungin {mones[index]} nimi:"))
    index += 1

for x in kaupunkiLista:
    print(x)
