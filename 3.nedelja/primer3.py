class Karta:

    kategorije ={"1": 1800, "2": 1600, "3":800, "4":500}  #atribut klase

    def __init__(self, predstava, oznaka, vreme, kategorija):
        self.predstava=predstava   #atributi instanci
        self.oznaka=oznaka
        self.vreme=vreme
        self.kategorija=kategorija

    def cena(self):
        return self.kategorije[self.kategorija]

    def __str__(self):
        return  f"Predstava: {self.predstava}, vreme {self.vreme}, mesto:{self.oznaka}"

class Kupovina:

    def __init__(self):
        self.karte=[]

    def dodajKartu(self, karta):
        self.karte.append(karta)

    def __str__(self):
        opis=""
        for karta in self.karte:
            opis+=str(karta) +"\n"
        return opis

    def ukupnoZaNaplatu(self, popust=0):
        zaNaplatu=0
        for karta in self.karte:
            zaNaplatu+=karta.cena()

        return zaNaplatu*(1-popust)

class Klijent:

    tipovi={'bronzani':0, 'srebrni':0.1, 'zlatni':0.2}  #atribut klase

    def __init__(self, ime, kontakt, tip="bronzani"):
        self.ime = ime   #atributi instanci
        self.kontakt = kontakt
        self.tip=tip
        self.kupovine=[]

    def dodajKupovinu(self, kupovina):
        self.kupovine.append(kupovina)

    def __getitem__(self, index):   #metod za citanje vrednosti pomocu indeksa
                                   #poziva se kada se navede objekat[indeks]
        return self.kupovine[index]

    def __str__(self):
        opis=f"Klijent: {self.ime}, tip: {self.tip}, kontakt: {self.kontakt}\n"
        i=1
        for kupovina in self.kupovine:
            opis+=f"Kupovna {i}\n{kupovina}"
            opis+=f"Za plaćanje: {kupovina.ukupnoZaNaplatu(self.tipovi[self.tip])} RSD\n\n"
            i+=1
        return opis


karta=Karta("Godine vrana", "Parter desno, red IX, mesto 5","15.3.2022. u 19.30", "1")
kupovina=Kupovina()
kupovina.dodajKartu(karta)
kupovina.dodajKartu(Karta("Godine vrana", "Parter desno, red IX, mesto 6","15.3.2022. u 19.30", "1"))
kupovina.dodajKartu(Karta("Godine vrana", "Parter desno, red IX, mesto 7","15.3.2022. u 19.30", "1"))

print('***kupovina***')
print(kupovina)

klijent = Klijent("Marko Markovic", "0635555555")
klijent.dodajKupovinu(kupovina)

kupovina.dodajKartu(Karta("Godine vrana", "Parter desno, red IX, mesto 8","15.3.2022. u 19.30", "1"))

print('***klijent[0]***')
print(klijent[0])  # izvrsavanje: klijent -> __getitem__(index=0)  -> klijent.kupovine[0] ->
                   # klijent.kupovine[0].__str__

kupovina2=Kupovina()
kupovina2.dodajKartu(Karta("Aida", "Galerija II levo, loža 1, mesto 1","22.3.2022. u 19.30", "2"))
kupovina2.dodajKartu(Karta("Aida", "Galerija II levo, loža 1, mesto 2","22.3.2022. u 19.30", "2"))

klijent.dodajKupovinu(kupovina2)

print('***klijent***')
print(klijent)
