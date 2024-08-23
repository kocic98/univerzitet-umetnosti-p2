class Racun:

    kursnaLista= {'EUR':0.00850, 'AUD':0.01281, 'USD':0.00927}  # atribut klase

    def __init__(self, id, vlasnik, stanje=0):
        self.id = id  #atibuti instanci
        self.vlasnik = vlasnik
        self.stanje = stanje

    def dodaj(self, vrednost):
        self.stanje += vrednost

    def skini(self, vrednost):
        if self.stanje < vrednost:
            print('Nema dovoljno sredstava na racunu')
            return False
        else:
            self.stanje -= vrednost
            return True

    def prenesi(self, racun, vrednost):
        if self.skini(vrednost):
            racun.dodaj(vrednost)
            print('Uspesan prenos')

    def __str__(self):
        return f"Racun: {self.id}, vlasnik {self.vlasnik}, tekuce stanje: {self.stanje}"

    @classmethod
    def konvertuj(cls, vrednost, valuta):
        return round(vrednost*cls.kursnaLista[valuta],3)


racun1=Racun(255, "Marko Markovic", 25600)
print(racun1)

print('skidanje 1000 sa racun1')
racun1.skini(1000)
print(racun1)

print('skidanje 50000 sa racun1')
racun1.skini(50000)
print(racun1)

print('dodavanje 50000 sa racun1')
racun1.dodaj(50000)
print(racun1)

racun2=Racun(658, "Petar Petrovic", 1000)
print(racun2)
print('prenos 25000 sa racun1 na racun2')
racun1.prenesi(racun2, 25000)
print(racun1)
print(racun2)

print(f"25000 rsd vredi {Racun.konvertuj(25000, 'EUR')} eur ili {Racun.konvertuj(25000, 'AUD')} aud.")
