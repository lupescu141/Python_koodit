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
        print(f"Rekisteritunnus | Nopeus | Kuljettu matka")
        print(f"{self.rekisteritunnus:^16}|{self.nopeus:^8}|{self.kuljettu_matka:^15}")

    def kiihdytin(self, speed):
        aloitusnopeus = self.nopeus
        self.nopeus = speed

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus


    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.nopeus


class Kilpailu():

    def __init__(self, nimi, pituus, osallistujat):

        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):

        for x in self.osallistujat:
            if x.kuljettu_matka >= self.pituus:
                return
            x.kiihdytin(random.randint(-10, 15))
            x.kulje(1)

    def tulosta_tilanne(self):

        for x in self.osallistujat:
            x.tiedot()

    def kilpailu_ohi(self):

        for x in self.osallistujat:

            if x.kuljettu_matka >= self.pituus:
                x.kuljettu_matka = self.pituus
                return True
        else:
            return False


osallistujat = []

for x in range(1, 11):
    osallistuja = Auto(f"ABC-{x}", random.randint(100, 200))
    osallistujat.append(osallistuja)

kilpailu = Kilpailu("Suuri romuralli", 8000, osallistujat)
kymmenen_valein = 0

while not kilpailu.kilpailu_ohi():
    kymmenen_valein += 1
    kilpailu.tunti_kuluu()

    if kymmenen_valein == 10:
        kilpailu.tulosta_tilanne()
        kymmenen_valein = 0
        print("__________________________________________________________________")

kilpailu.tulosta_tilanne()


