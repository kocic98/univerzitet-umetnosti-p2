# Klase 
	
	class ImeKlase:
	
		#definisanje članova klase - atributa i metoda
		
		def __init__(self, arg1, arg2=20): # f-ja koja se automatski izvršava kada se pravi novi objekat
		
			self.atribut1=arg1    #definišu se atributi (polja)
			self.atribut2=arg2
			self.atribut3="Vrednost"
			
		def metod1(self, arg1, arg2, ..., argN):  #f-ja pomoću koje se implementira ponašanje klase - metod
		
	objekat=ImeKlase(arg1V, arg2V)
	print(objekat.atribut1)
	objekat.metod1()
		


1. Napraviti klasu **Student** koja opisuje studente.
* Od atributa klasa sadrži:
 	* **ime**
 	* **prezime**
	* **indeks**  (koji se zadaje kao ceo broj  u obliku GGGGXXXX, gde je GGGG grodina upisa na fakultet, a XXXX jedinstven broj studenta na nivou godine, npr. 20210256)
	* **prosek** koji kao podrazumevanu vrednost ima 0
* Napisati konstruktor za klasu.
* Obezbediti metode:
  * **formatiranIndeks** - koja vraća broj indeksa u obliku XXXX/GGGG
  * metod za predstavljanje objekta klase kao niske
* Napraviti objekat klase **Student** koja predstavlja studenta Marka Markovića sa indeksom 20200235. Postaviti i da je student rođen u Beogradu.


2. Napraviti klasu **Student** koja opisuje studente.
* Od atributa klasa sadrži:
 	* **ime**
 	* **prezime**
	* **indeks**  - zadaje se kao ceo broj  u obliku GGGGXXXX, gde je GGGG grodina upisa na fakultet, a XXXX jedinstven broj studenta na nivou godine, npr. 20210256)
	* **ispiti** koji sadrži listu ispita studenta. Svaki element liste sadrži naziv predmeta koji je student polagao i ocenu koju je student dobio na ispitu.
* Napisati konstruktor za klasu.
* Obezbediti metode:
  * **formatiranIndeks** - vraća broj indeksa u obliku XXXX/GGGG
  * metod za predstavljanje objekta klase kao niske
  * **dodajIspit** - u listu ispita dodaje podatak o novom ispitu koji je student polagao 
  * **ispisiPolozeneIspite** - ispisuje podatke o položenim ispitima
  * **prosek** - vraća prosečnu ocenu studenta dobijenu na položenim ispitima
* Napraviti objekat klase **Student** koja predstavlja studenta Marka Markovića sa indeksom 20200235. Postaviti i da je student rodjen u Beogradu.
* Student je polagao ispite iz sledećih predmeta
   * Programiranje 1 i dobio je ocenu 8
   * Digitalni zapis podataka i dobio je ocenu 10
   * 3D modeli i dobio je ocenu 10
* Ispisati podatke o položenim ispitima studenta.
* Ispisati prosek studenta.

3. Napraviti klasu **Pitanje** koja opisuje jedno pitanje u Kvizu. 
* Od atributa klasa sadrži atribut za pitanje, po jedan atribut za 4 moguća odgovora i atribut za redni broj tačnog odgovora. 
* Napisati konstruktor za klasu.
* Obezbediti metode:
  * **postaviPitanje** - ispisuje pitanje i moguće odgovore
  * **proveriOdgovor** - proverava da li je zadati odgovor tačan ili ne i vraća True ako jeste, a False ako nije.
* Napraviti objekat klase **Pitanje**

