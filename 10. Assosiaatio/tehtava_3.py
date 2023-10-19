class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):

        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

    def siirry_kerrokseen(self,siirtyy_kerrokseen):

        while siirtyy_kerrokseen < self.kerros > self.alin_kerros:
            self.kerros_alas()
            print(f"Laskee kerrokseen:{self.kerros}")

        while siirtyy_kerrokseen > self.kerros < self.ylin_kerros:
            self.kerros_ylös()
            print(f"Nousee kerrokseen:{self.kerros}")


class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):

       self.alin_kerros = alin_kerros
       self.ylin_kerros = ylin_kerros
       self.hissien_maara = hissien_maara
       self.hissit = []

       for x in range(1, self.hissien_maara + 1):

           hissi = Hissi(self.alin_kerros, self.ylin_kerros)
           self.hissit.append(hissi)

    def aja_hissiä(self, kohde_hissi, kohde_kerros):

        print(f"Talon hissi{kohde_hissi}:")

        try:
            self.hissit[kohde_hissi - 1].siirry_kerrokseen(kohde_kerros)

        except:
                print("Hissiä ei ole olemassa!")

    def palohalytys(self):

        print(f"Talossa tulipalo! Hissit siirtyvät kerrokseen:{self.alin_kerros}")
        kierros = 0

        for x in self.hissit:
            kierros += 1
            print(f"Talon Hissi {kierros}:")
            x.siirry_kerrokseen(self.alin_kerros)


talo = Talo(1, 6, 5)
talo.aja_hissiä(4, 4)
talo.aja_hissiä(2, 5)
talo.palohalytys()