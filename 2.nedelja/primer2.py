class Osoba:
    def __init__(self, ime, prezime, jmbg, telefon):   #konstruktor
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg
        self.telefon=telefon

        #obratiti paznju da je 'ime' lokalna promenljiva u metodi, a
        # self.ime clanica instance
        #isto vazi i za parove  prezime/self.prezime, jmbg/self.jmbg, telefon/self.telefon

    def datumRodjenja(self):
        dan = self.jmbg[:2]
        mesec = self.jmbg[2:4]
        godina = self.jmbg[4:7]
        godina = '2' + godina if godina[0] == '0' else '1' + godina

        return f'{dan}.{mesec}.{godina}.'

    def __str__(self):
        return f'{self.ime} {self.prezime} ima jmbg {self.jmbg}. Kontakt je {self.telefon}.'

class Student(Osoba):

    def __init__(self, ime, prezime, indeks, jmbg, telefon):

        super().__init__(ime, prezime, jmbg, telefon)
        # ili
        #Osoba.__init__(self, ime, prezime, jmbg, telefon)

        self.indeks=indeks
        self.ispiti = []

    def formatiranIndeks(self):
        return f"{self.indeks%10000}/{int(self.indeks/10000)}"

    def dodajIspit(self, predmet, ocena):
        self.ispiti.append((predmet,ocena))

    def polozeniIspiti(self):
        opis=""
        for i in self.ispiti: #prolazak kroz listu ispita

            if i[1]>=6:
                opis += f"Predmet: {i[0]}, ocena: {i[1]}\n"

        if opis=="":
            return "Nema položenih ispita"
        else:
            return opis

    def prosek(self):

        zbir=0
        ukupanBroj=0

        for i in self.ispiti:
            if i[1] >= 6:
                zbir += i[1]
                ukupanBroj += 1

        if ukupanBroj > 0:
            return round(zbir/ukupanBroj, 2)
        else:
            return 0

    def __str__(self):

        return super().__str__() + \
               f" Indeks studenta je {self.indeks}, a prosek {self.prosek()}.\n" + \
               "Lista položenih ispita je:\n" + self.polozeniIspiti()


class Nastavnik(Osoba):

    def __init__(self, ime, prezime, jmbg, telefon, zvanje, koeficijent=20.0):

        super().__init__( ime, prezime, jmbg, telefon)
        self.zvanje=zvanje
        self.koeficijent=koeficijent

    def plata(self):
        return self.koeficijent*3500

    def __str__(self):
        return super().__str__() + f"\nZvanje {self.zvanje} sa platom {self.plata()}\n"

pera = Osoba('Petar', 'Petrovic', '1009995555555', '0635555555')
print(pera.ime, pera.prezime)
print(pera.datumRodjenja())

andja = Osoba('Andja', 'Lalic', '0512002888888', '0659999999')
print(andja.datumRodjenja())
print(andja)

student1 = Student('Jovan', 'Paunovic', '125/2019', '0307001999999', '0638888888')
student1.dodajIspit('Programiranje 1', 10 )
student1.dodajIspit('Programiranje 2', 9)
student1.dodajIspit('DZP', 5)
print(student1)

asistent = Nastavnik("Ana", "Petrovic", "0506979888888", "0637777777", "docent", koeficijent=22)
print(asistent)
