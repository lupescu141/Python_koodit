import math

class Pizza:
    yksikkohinta = 0.0

    def __init__(self, halkaisija, hinta):
        self.halkaisija = float(halkaisija)
        self.hinta = float(hinta)


def piza_laskin (halkaisija, hinta):
    pinta_ala_neliometreina = ((halkaisija / 2 / 100) ** 2) * math.pi
    yksikkohinta = hinta / pinta_ala_neliometreina
    return yksikkohinta


print("Kirjoita ensimmäisen pizzan:")
pizza1 = Pizza(input("Halkaisija senttimetreinä:"), input("hinta:"))
pizza1.yksikkohinta = piza_laskin(pizza1.halkaisija, pizza1.hinta)

print("Kirjoita toisen pizzan:")
pizza2 = Pizza(input("Halkaisija senttimetreinä:"), input("hinta:"))
pizza2.yksikkohinta = piza_laskin(pizza2.halkaisija, pizza2.hinta)

if (pizza1.yksikkohinta < pizza2.yksikkohinta):
    print(f"Pizzojen yksikköhinnat ovat:")
    print(f"pizza1 = {pizza1.yksikkohinta :.2f} e/m2")
    print(f"pizza2 = {pizza2.yksikkohinta :.2f} e/m2")
    print("Esnimmäinen pizza antaa paremman vasineen rahalle!")

elif(pizza1.yksikkohinta > pizza2.yksikkohinta):
    print(f"Pizzojen yksikköhinnat ovat:")
    print(f"pizza1 = {pizza1.yksikkohinta :.2f} e/m2")
    print(f"pizza2 = {pizza2.yksikkohinta :.2f} e/m2")
    print("Toinen pizza antaa paremman vasineen rahalle!")

else:
    print(f"Pizzojen yksikköhinnat ovat:")
    print(f"pizza1 = {pizza1.yksikkohinta :.2f} e/m2")
    print(f"pizza2 = {pizza2.yksikkohinta :.2f} e/m2")
    print("Pizzat ovat samanarvoisia")
