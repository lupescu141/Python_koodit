class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka=0, nopeus=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = kuljettu_matka
        self.nopeus = nopeus

    nopeus = 0
    kuljettu_matka = 0

    def tiedot(self):
        return (f"\nRekisteritunnus: {self.rekisteritunnus}\n\n"
                f"Huippunopeus: {self.huippunopeus}\n\n"
                f"Tämänhetkinen nopeus: {self.nopeus}\n\n"
                f"Kuljettu matka: {self.kuljettu_matka}\n\n")

    def kiihdytin(self, speed):
        aloitusnopeus = self.nopeus
        self.nopeus = speed

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus

        if self.nopeus < aloitusnopeus:
            print(f"Auto jarruttaa nopeuteen: {self.nopeus}km/h\n")
        elif self.nopeus > aloitusnopeus:
            print(f"Auto kiihdyttää nopeuteen: {self.nopeus}km/h\n")

    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.nopeus
        print(f"Tämän hetkinen kuljettu matka on {int(self.kuljettu_matka)}km. Nopeus on {self.nopeus}km/h")


class Sahkoauto(Auto):

    def __init__(self, rekistetitunnus, huippunopeus, akkukapasiteetti):

        super().__init__(rekistetitunnus, huippunopeus)
        self.akkukapiseteetti = akkukapasiteetti


class Polttomottoriauto(Auto):

    def __init__(self, rekistetitunnus, huippunopeus, bensatankin_koko):

        super().__init__(rekistetitunnus, huippunopeus)
        self.beansatankin_koko = bensatankin_koko


abc15 = Sahkoauto("ABC-15", 180, 52.5)
acd123 = Polttomottoriauto("ACD-123", 165, 32.3)

abc15.kiihdytin(125)
acd123.kiihdytin(130)

abc15.kulje(3)
acd123.kulje(3)

abc15.tiedot()
acd123.tiedot()