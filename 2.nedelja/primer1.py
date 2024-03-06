class Student:

    univerzitet ="Univerzitet umetnosti"  #atribut klase

    def __init__(self, ime, prezime, indeks, prosek=0):
        self.ime=ime  #atributi instance
        self.prezime=prezime
        self.indeks=indeks
        self.prosek=prosek

    @classmethod  #klasni metod
    def kontakt(cls):
        #print(self.ime)  #ne moze
        return cls.univerzitet + ", Kosancicev venac 29"

    @staticmethod  #staticki metod
    def godinaIzIndeksa(brojIndeksa):
        return int(brojIndeksa/10000)

    def formatiranIndeks(self):
        return f"{self.indeks%10000}/{int(self.indeks/10000)}"

    def __str__(self):
        opis=f"Student {self.ime} {self.prezime} ima indeks {self.indeks} i prosek {self.prosek}"
        if hasattr(self, "mestoRodjenja"):
            opis+=f" a mesto rodjenja mu je {self.mestoRodjenja}"
        return opis


student=Student("Marko", "Markovic", 20200235)
print(student)

student.mestoRodjenja="Beograd"
print(student)

print("kalsa Student", Student.univerzitet)
#print(Student.ime)  #prijavljuje gresku
print("objekat student", student.univerzitet)

student.univerzitet ="Univerzitet u Beogradu"

print("objekat student", student.univerzitet)

Student.univerzitet ="Univerzitet u Novom Sadu"
print("klasa Student", Student.univerzitet)
print("objekat student", student.univerzitet)

student2=Student("Petar", "Petrovic", 20210155)
print(student2)
print("objekat student2",student2.univerzitet)


print("klasa Student", Student.kontakt())
print("objekat student", student.kontakt())
print("objekat student2", student2.kontakt())

print("klasa Student", Student.godinaIzIndeksa(20160258))
print("objekat student", student.godinaIzIndeksa(student.indeks))
print("objekat student", student.godinaIzIndeksa(20160258))
