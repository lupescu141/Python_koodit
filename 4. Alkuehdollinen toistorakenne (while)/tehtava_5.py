userName = "python"
password = "rules"
arvausKerrat = 0

while arvausKerrat < 5:

    userInputName = input("Syötä käyttäjän tunnus:")
    userInputPassword = input("Syötä käyttäjän salasana")

    if userInputName == userName and userInputPassword == password:
        print("Tervetuloa")
        break

    else:
        print("Kirjautumis tiedot ovat virheelliset")
        arvausKerrat += 1

if arvausKerrat == 5:
    print("Pääsy evätty")
