import random


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
            print(f"{self.rekisteritunnus} jarruttaa nopeuteen: {self.nopeus}km/h\n")
        elif self.nopeus > aloitusnopeus:
            print(f"{self.rekisteritunnus} kiihdyttää nopeuteen: {self.nopeus}km/h\n")

    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.nopeus
        print(f"{self.rekisteritunnus} kuljettu matka on {int(self.kuljettu_matka)}km. Nopeus on {self.nopeus}km/h")


kilpailijat = []

for x in range(1, 11):
    kilpailija = Auto(f"ABC-{x}", random.randint(100, 200))
    kilpailijat.append(kilpailija)

kilpailu_ohi = False

while not kilpailu_ohi:

    for x in kilpailijat:
        x.kiihdytin(random.randint(-10, 15))
        x.kulje(1)

        if x.kuljettu_matka >= 10000:

            x.kuljettu_matka = 10000
            print(f"Voittaja on: {x.rekisteritunnus}")
            kilpailu_ohi = True
            break

for x in kilpailijat:
    print(x.tiedot())
