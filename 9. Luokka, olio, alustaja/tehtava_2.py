
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

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


ferrari = Auto("ABC-123", 142)
ferrari.kiihdytin(+30 + 70 + 50)
ferrari.kiihdytin(-200)