suorakulmionKanta = input('Kirjoita suorakulmion kanta:')

while any(c.isalpha() for c in suorakulmionKanta):
    print("Kirjoita vain numeroita kiitos!")
    suorakulmionKanta = input('Kirjoita ympyrän säde:')

suorakulmionKorkeus = input('Kirjoita suorakulmion korkeus:')

while any(c.isalpha() for c in suorakulmionKorkeus):
    print("Kirjoita vain numeroita kiitos!")
    suorakulmionKorkeus = input('Kirjoita ympyrän korkeus:')

suorakulmionPiiri = float(suorakulmionKorkeus) * 2 + float(suorakulmionKanta) * 2
suorakulmionPintaAla = float(suorakulmionKorkeus) * float(suorakulmionKanta)

print("Suorakulmion piiri on: ",  suorakulmionPiiri)
print("Suorakulmion pinta-ala on: ",  suorakulmionPintaAla)


