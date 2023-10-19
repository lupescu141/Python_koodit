class Julkaisu:

    def __init__(self, nimi):

        self.nimi = nimi


    def tulosta_tiedot(self):

        print(f"Julkaisun nimi: {self.nimi}")


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):

        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}\n")


class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):

        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}\n"
              f"Sivumäärä: {self.sivumaara}\n")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", "200 sivua")

aku_ankka.tulosta_tiedot()
hytti6.tulosta_tiedot()



