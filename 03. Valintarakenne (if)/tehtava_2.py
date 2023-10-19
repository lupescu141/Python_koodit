LUX = "LUX on parvekkeellinen hytti yläkannella."
A = "A on ikkunallinen hytti autokannen yläpuolella."
B = "B on ikkunaton hytti autokannen yläpuolella."
C = "C on ikkunaton hytti autokannen alapuolella."

i = 0
while i < 1:
    hyttiluokka = input("Valitse jokin hyttiluokista: LUX, A, B, C :")

    if hyttiluokka.upper() == "LUX":
        print(LUX)
        i += 1
        break

    elif hyttiluokka.upper() == "A":
        print(A)
        i += 1
        break

    elif hyttiluokka.upper() == "B":
        print(B)
        i += 1
        break

    elif hyttiluokka.upper() == "C":
        print(C)
        i += 1
        break

    else:
        print("Virheellinen hyttiluokka")
