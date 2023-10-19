def kuhan_laskin(mitattava_kala):
    alamitta = 37
    tulos = 0

    if (mitattava_kala < alamitta):
        tulos = alamitta - mitattava_kala
        print(f"Laske kuha vapaaksi! Sinulta puuttuu {tulos :.2f} senttiä sallitusta alimitasta")

kuha = float(input("Hei sinä kalamies siellä! Kerro minulle kuinka suuri on kuhasi senttimetreinä:"))
kuhan_laskin(kuha)


