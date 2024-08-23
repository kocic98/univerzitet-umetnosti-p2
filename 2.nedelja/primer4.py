class Pitanje:
    def __init__(self, pitanje, odgovor1, odgovor2, odgovor3, odgovor4, tacanOdgovor):
        self.pitanje=pitanje
        self.odgovor1=odgovor1
        self.odgovor2=odgovor2
        self.odgovor3=odgovor3
        self.odgovor4=odgovor4
        self.tacanOdgovor=tacanOdgovor

    def proveriOdgovor(self, odgovor):
        if odgovor==self.tacanOdgovor:
            return True
        return False

    def postaviPitanje(self):
        return f"Pitanje: {self.pitanje}\nMogući odgovori:\n" \
               f"1){self.odgovor1}\n" \
               f"2){self.odgovor2}\n" \
               f"3){self.odgovor3}\n" \
               f"4){self.odgovor4}\n"


class Kviz:
    def __init__(self):
        self.pitanja=[]

    def dodajPitanje(self, pitanje, odgovor1, odgovor2, odgovor3, odgovor4, tacanOdgovor):
        self.pitanja.append(Pitanje(pitanje, odgovor1, odgovor2, odgovor3, odgovor4, tacanOdgovor))

    def pokreniKviz(self):

        brojTacnihOdgovora = 0

        for p in self.pitanja:
            print(p.postaviPitanje())
            odgovor = input("Unesite redni broj Vašeg odgovora:")
            if p.proveriOdgovor(odgovor):
                print("Vaš odgovor je tačan")
                brojTacnihOdgovora += 1
            else:
                print("Vaš odgovor nije tačan")
            print("\n")

        print(f"Ukupan broj tačnih odgovora: {brojTacnihOdgovora}")

kviz=Kviz()
kviz.dodajPitanje("Koliko različitih vremenskih zona ima na zemlji?",
            "36", "12", "48", "24", "4")

kviz.dodajPitanje("Koje je ime najčešće na svetu?",
            "Abdul", "Muhamed", "Wong", "Petar", "2")


kviz.dodajPitanje(pitanje="Koje je godine prvi put održano svetsko prvenstvo u fudbalu u Meksiku?",
                       odgovor1="1962.",
                       odgovor3="1986.",
                       odgovor2="1970.",
                       odgovor4="1982.",
                       tacanOdgovor="2")


kviz.dodajPitanje("Koju zajedničku boju imaju zastave Andore, Belgije, Bosne i Hercegovine i Litvanije?",
               "Crvena", "Crna", "Žuta", "Plava", "3")
kviz.dodajPitanje("Kako se naziva gubitak sposobnosti čitanja?",
                       "Aleksija", "Maksija", "Saksija", "Feliksija", "1")

kviz.pokreniKviz()