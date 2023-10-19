
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


ferrari = Auto("ABC-123", 142)

print(ferrari.tiedot())
