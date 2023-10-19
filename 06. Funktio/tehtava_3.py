def litraMuunnin (gallonamäärä):
    return float(gallonamäärä * 3.785)

while True:
    userInput = input("Ilmoita gallonamäärä:")

    if float(userInput) < 0:
        break

    else:
        print(f"{userInput} gallonaa = {litraMuunnin(float(userInput)) :.2f} litraa")