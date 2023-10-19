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



h = Hissi(1, 10)
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(1)