class Student:

    def __init__(self, ime, prezime, indeks, prosek=0):
        self.ime = ime
        self.prezime = prezime
        self.indeks = indeks
        self.ispiti = []   # 1 element liste je 1 ispit i element je n-torka u obliku (nazivPredmeta, ocena)
                           #  ako student ima 2 ispita lista ce imati 2 elementa i izgledati: # [(nazivPredmeta1, ocena1), (nazivPredmeta2, ocena2)]

    def formatiranIndeks(self):
        return f"{self.indeks%10000}/{int(self.indeks/10000)}"

    def __str__(self):

        opis = f"Student {self.ime} {self.prezime} ima indeks {self.indeks}"

        if hasattr(self, "mestoRodjenja"):
            opis+= f" a mesto rodjenja mu je {self.mestoRodjenja}"

        return opis

    def dodajIspit(self, predmet, ocena):
        self.ispiti.append((predmet,ocena))

        #podsecanje:
        # append - dodaje novi element na kraj liste, npr.
        # x=[]
        # x.append(5)  - > x = [5]
        # x.append(10)  - > x = [5, 10]


    def ispisiPolozeneIspite(self):

        for i in self.ispiti: #prolazak kroz listu ispita

            if i[1]>=6:  #za svaki ispit, koji je n-torka (nazivPredmeta, ocena),
                         # se proverava da li je polozen

                         #podsecanje: vrednostima u okviru n-torke pristupamo preko indeksa
                         #u (nazivPredmeta, ocena)
                         #nazivPredmeta ima indeks 0
                         #a ocena indeks 1

                print(f"Predmet: {i[0]}, ocena: {i[1]}")


        #Ako je self.ispiti [ ('Programiranje 1', 8)  ,  ('DZP', 10) ,    ('3D modeli', 5)]
        #rezultat petlje  for i in self.ispiti je
            # 1.korak :i -> ('Programiranje 1', 8)
            # 2.korak: i -> ('DZP', 10)
            # 3.korak: i-> ('3D modeli', 5)

    def prosek(self):

        #lokalne promenljive u okviru metoda
        zbir=0
        ukupanBroj=0

        for i in self.ispiti:
            if i[1] >= 6:
                zbir += i[1]
                ukupanBroj += 1

        if ukupanBroj > 0: #provera da li student ima polozen ispit
            return round(zbir/ukupanBroj, 2)
        else:
            return 0


student1 = Student("Marko", "Markovic", 20200235)
print(student1.indeks, student1.ime)
student1.mestoRodjenja = "Beograd"

student2 = Student("Petar", "Petrovic", 20210155)
print(student2.indeks, student2.ime, student2.prosek)

formatiranIndeks = student2.formatiranIndeks()
#print(formatiranIndeks)

print(student1)
print(student1.mestoRodjenja)
print(student2)

student1.dodajIspit("Programiranje 1", 8)
print(student1.ispiti)

print(student1.ispiti[0])
print("naziv predmeta", student1.ispiti[0][0])
print("ocena", student1.ispiti[0][1])

student1.dodajIspit("DZP", 10)
print(student1.ispiti)
print("ocena", student1.ispiti[1][1])

student1.dodajIspit("3D modeli", 5)
student1.dodajIspit("Programiranje 2", 10)
student1.ispisiPolozeneIspite()

print(student1.prosek())
