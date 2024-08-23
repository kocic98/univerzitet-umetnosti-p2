class Pitanje:

    def __init__(self, pitanje, odgovor1, od2, odgovor3, odgovor4, tacanOdgovor):
        self.pitanje = pitanje
        self.odgovor1 = odgovor1
        self.odgovor2 = od2
        self.odgovor3 = odgovor3
        self.odgovor4 = odgovor4
        self.tacanOdgovor = tacanOdgovor

    def postaviPitanje(self):
        print(self.pitanje)
        print('Mogući odgovori:')
        print("1)", self.odgovor1)
        print("2)", self.odgovor2)
        print("3)", self.odgovor3)
        print("4)", self.odgovor4)

    def proveriOdgovor(self, odgovorTakmicara):
        if odgovorTakmicara == self.tacanOdgovor:
            return True
        else:
            return False

p=Pitanje(pitanje="Koliko različitih vremenskih zona ima na zemlji?",
          od2="36", tacanOdgovor="4",
          odgovor1="12", odgovor3="48", odgovor4="24"
          )
p.postaviPitanje()

odgovor = input("Unesite redni broj Vašeg odgovora: ")

if p.proveriOdgovor(odgovor):
    print("Vaš odgovor je tačan")
else:
    print("Vaš odgovor nije tačan")
