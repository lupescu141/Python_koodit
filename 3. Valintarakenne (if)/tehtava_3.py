def hemo_laskin(sukupuoli,hemoglobiini):

    if str.upper(sukupuoli) == "MIES":
        if 134 <= hemoglobiini < 195:
            print("Sinun hemoglobiiniarvo on normaali!")

        elif hemoglobiini < 134:
            print("Sinun hemoglobiiniarvo on matala!")

        elif hemoglobiini > 195:
            print("Sinun hemoglobiiniarvo on korkea!")

    if str.upper(sukupuoli) == "NAINEN":
        if 117 <= hemoglobiini < 175:
            print("Sinun hemoglobiiniarvo on normaali!")

        elif hemoglobiini < 117:
            print("Sinun hemoglobiiniarvo on matala!")

        elif hemoglobiini > 175:
            print("Sinun hemoglobiiniarvo on Korkea!")


userinput = ''
sukupuoli = ''
hemoglobiini = ''

i = 0

while i < 1:
        userinput = input("Oletko 'MIES' vai 'NAINEN'")
        if str.upper(userinput) == "MIES" or str.upper(userinput) == "NAINEN":
            sukupuoli = userinput
            i += 1

i = 0

while i < 1:
        userinput = input("Kerro hemoglobiiniarvosi:")
        if userinput.isdigit():
            hemoglobiini = int(userinput)
            i += 1

hemo_laskin(sukupuoli, hemoglobiini)