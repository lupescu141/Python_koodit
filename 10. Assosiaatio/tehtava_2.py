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

        while siirtyy_kerrokseen < self.kerros < self.alin_kerros:
            self.kerros_alas()
            print(f"Hissi laskee kerrokseen:{self.kerros}")

        while siirtyy_kerrokseen > self.kerros < self.ylin_kerros:
            self.kerros_ylös()
            print(f"Hissi nousee kerrokseen:{self.kerros}")


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


talo = Talo(1, 6, 5)
talo.aja_hissiä(4, 4)
