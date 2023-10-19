lentoasemat = {"EFET": "Enontekiön lentoasema",
               "EFHK": "Helsinki-Vantaan lentoasema",
               "EFIV": "Ivalon lentoasema",
               "EFJO": "Joensuun lentoasema",
               "EFKI": "Kajaanin lentoasema",
               "EFKE": "Kemi-Tornion lentoasema",
               "EFKT": "Kittilän lentoasema",
               "EFKK": "Kokkola-Pietarsaaren lentoasema",
               "EFKS": "Kuusamon lentoasema",
               "EFLP": "Lappeenrannan lentoasema",
               "EFMA": "Maarianhaminan lentoasema",
               "EFMI": "Mikkelin lentoasema",
               "EFOU": "Oulun lentoasema",
               "EFPO": "Porin lentoasema",
               "EFSA": "Savonlinnan lentoasema",
               "EFSI": "Seinäjoen lentoasema",
               "EFTU": "Turun lentoasema",
               "EFVA": "Vaasan lentoasema"}

while True:
    print("Käskyt ovat sulkujen sisällä:  (syötä)  (hae)  (lopeta)")
    command = input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa ohjelman:")

    if command.lower() == "syötä":

        while True:
            icao = input("Syötä lentokentän ICAO-koodi:").upper()

            if len(icao) == 4 and not icao.isdigit():
                break
            else:
                print("Syötteeksi käy vain 4 kirjaiminen ICAO-koodi")

        while True:
            lentokentän_nimi = input("Syötä lentokentän nimi:")

            if lentokentän_nimi.strip() == '':
                continue
            else:
                print(f"Lentokenttä {lentokentän_nimi} lisätty!")
                break

        lentoasemat[icao] = lentokentän_nimi

    elif command.lower() == "hae":

        while True:
            haku = input("Hae lentokenttiä kirjoittamalla ICAO-koodi, jos haluat lopettaa haen kirjoita (lopeta):")

            if haku.lower() == "lopeta":
                break

            else:
                try:
                    lentoasemat[haku.upper()]
                except:
                    print(f"Haulla {haku} ei löytynyt lentokenttiä!")
                else:
                    print(f"Haulla {haku.upper()}, löytyi: {lentoasemat[haku.upper()]}")

    elif command.lower() == "lopeta":
        break

