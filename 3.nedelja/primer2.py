class Predstava:

    def __init__(self, naziv, reditelj, premijera, izvodjaci=[]):
        self.naziv=naziv
        self.premijera=premijera
        self.reditelj=reditelj
        self.izvodjaci = izvodjaci

    def dodajIzvodjaca(self, izvodjac):
        self.izvodjaci.append(izvodjac)

    def ispisiIzvodjace(self):
        izvodjaci=""
        for izvodjac in self.izvodjaci:
            izvodjaci+=izvodjac + "\n"
        return izvodjaci

    def __str__(self):
        return f"{self.naziv}\n" \
               f"Premijera: {self.premijera}\n" \
               f"Reditelj: {self.reditelj}\n" \
               f"Uloge:\n{self.ispisiIzvodjace()}"

class Drama(Predstava):

    def __init__(self, naziv, pisac, reditelj, dramaturg, premijera, igraju=[]):

        super().__init__(naziv, reditelj, premijera, igraju)
        self.pisac=pisac
        self.dramaturg=dramaturg

    def __str__(self):
        return super().__str__() + \
               f"Pisac: {self.pisac}\n" \
               f"Dramaturg: {self.dramaturg}\n"


class Opera(Predstava):

    def __init__(self, naziv, kompozitor, reditelj, dirigent,  premijera, izvodjaci=[]):
        super().__init__(naziv, reditelj, premijera, izvodjaci)
        self.kompozitor = kompozitor
        self.dirigent = dirigent

    def __str__(self):
        return super().__str__() + \
               f"Kompozitor: {self.kompozitor}\n" \
               f"Dirigent: {self.dirigent}\n"


drama=Drama("Godine vrana", "Siniša Kovačević","Siniša Kovačević",
                "Danka Sekulović", "12.3.2022.",
                igraju=["Kalnina Kovačević", "Aleksandar Srećković"])

drama.dodajIzvodjaca("Petar Strugar")
drama.dodajIzvodjaca("Ljiljana Blagojević")
drama.dodajIzvodjaca("...")

print(drama.ispisiIzvodjace())

print(drama)


opera=Opera("Aida", "Đuzepe Verdi","Ognjan Draganov",
                "Đorđe Pavlović", "10.4.2013.")

opera.dodajIzvodjaca("Stefan Pavlović")
opera.dodajIzvodjaca("Jelena Vlahović")
opera.dodajIzvodjaca("Jasmina Trumbetaš Petrović")
opera.dodajIzvodjaca("...")

print(opera)
