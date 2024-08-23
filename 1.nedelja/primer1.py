class Student:

    def __init__(self, ime, prezime, indeks, prosek=0):
        self.ime = ime
        self.prezime = prezime
        self.indeks = indeks
        self.prosek = prosek   #ceo broj u obliku GGGGXXXX

    def formatiranIndeks(self):  #povratna vrednost je u obliku XXXX/GGGG
        return f"{self.indeks%10000}/{int(self.indeks/10000)}"

        #primer
        #ako je indeks 20210155
        # self.indeks%10000 -> 155
        # int(self.indeks/10000)  -> int(2021.0155) -> 2021

    def __str__(self):    # koristi se pri pozivu str(objekat) ili   print(objekat)

        opis = f"Student {self.ime} {self.prezime} ima indeks {self.indeks} i prosek {self.prosek}"

        if hasattr(self, "mestoRodjenja"):   #provera da li instanca ima atribut mestoRodjenja
            opis+= f" a mesto rodjenja mu je {self.mestoRodjenja}"

        return opis

        #podsecanje:
        # ako je
        # imeProm=5
        # imeProm2="abc"
        # onda je
        # f"{imeProm}TT{imeProm2}"  -> "5TTabc"


student1 = Student("Marko", "Markovic", 20200235, 8.0)
print(student1.indeks, student1.ime, student1.prosek)
student1.mestoRodjenja = "Beograd"  #dodavanje atributa instanci

student2 = Student("Petar", "Petrovic", 20210155)
#print(student2.indeks, student2.ime, student2.prosek)

formatiranIndeks = student2.formatiranIndeks()
print(formatiranIndeks)

print(student1)  # poziva student1.__str__()
print(student1.mestoRodjenja)
print(student2)  #  poziva student2.__str__()
