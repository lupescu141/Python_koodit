
def laske_massa(laskettava_kohde, massalista):

    luoti = float(13.3)
    naula = luoti * 32
    leiviska = naula * 20

    if laskettava_kohde[0]:
        massalista.append(float(laskettava_kohde[0] * leiviska))

    if laskettava_kohde[1]:
        massalista.append(float(laskettava_kohde[1] * naula))

    if laskettava_kohde[2]:
        massalista.append(float(laskettava_kohde[2] * luoti))


vastaus = float
massat = []
userInputs = []
kaskyLista = ["Anna leiviskät. ", "Anna naulat. ", "Anna luodit. "]

i = 0

while i < 3:
    userInput = input(kaskyLista[i])

    if any(c.isalpha() for c in userInput) or (len(userInput) == 0):
        print("numeroina")

    else:
        userInputs.append(float(userInput))
        i += 1

laske_massa(userInputs, massat)

yhteen = (massat[0] + massat[1] + massat[2]) / 1000
vastausKiloina = int(yhteen)
vastausGrammoina = (yhteen - vastausKiloina) * 1000

print("Massa nykymittojen mukaan:")
print(f"{vastausKiloina} kilogrammaa ja  {vastausGrammoina: .2f}  grammaa.")
