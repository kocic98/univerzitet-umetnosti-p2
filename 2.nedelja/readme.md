# Klase 
```python
	class ImeKlase:
	
		#definisanje članova klase - atributa i metoda
		
		cls_atribut1 = vrednost1   #definišu se klasni atributi 
		cls_atribut2 = vrednost2
		
		def __init__(self, arg1, arg2=20): # f-ja koja se automatski izvršava kada se pravi novi objekat (instanca)
		
			self.atribut1=arg1    #definišu se atributi instance
			self.atribut2=arg2
			self.atribut3=vrednost3
			
		def metod1(self, arg1, arg2, ..., argN):  #metod koji može da pozove instanca klase

			...
			#bitno:
				#mogu da se koriste klasni atributi navođenjem self.cls_atribut1 ili self.cls_atribut2
				#mogu da se koriste atributi instance navođenjem self.atribut1, self.atribut2, ...
				#upotreba 
				   #instanca.metod1(arg1, arg2, ..., argN) 
				      
			
		@classmethod
		def metod2(cls, arg1, arg2, ..., argN):  #klasni metod
			...	
			#bitno:
				#mogu da se koriste klasni atributi navođenjem cls.cls_atribut1 ili cls.cls_atribut2
				#ne mogu da se koriste atributi instance (atribut1, atribut2 ili atribut3)
				
				#upotreba 
				   # ImeKlase.metod2(arg1, arg2, ..., argN) ili
				   # instanca.metod2(arg1, arg2, ..., argN)

	
		@staticmethod
		def metod3(arg1, arg2, ..., argN):  #statički metod
			...	
			#bitno:
				#ne mogu da se koriste ni klasni atributi ni atributi instance 
				#upotreba 
				   # ImeKlase.metod3(arg1, arg2, ..., argN) ili
				   # instanca.metod3(arg1, arg2, ..., argN) 
		
	objekat=ImeKlase(arg1V, arg2V)
	print(objekat.atribut1)
	objekat.metod1()
	
	ImeKlase.metod2(arg1V, arg2V, ..., argNV)	
	objekat.metod2(arg1V, arg2V, ..., argNV)	


	ImeKlase.metod3(arg1V, arg2V, ..., argNV)	
	objekat.metod3(arg1V, arg2V, ..., argNV)	
```

1. Napraviti klasu **Student** koja opisuje studente.
	* Od atributa sadrži:
		* atribute koji opisuju instance
			* **ime**
			* **prezime**
			* **indeks**  (koji se zadaje kao ceo broj  u obliku GGGGXXXX, gde je GGGG grodina upisa na fakultet, a XXXX jedinstven broj studenta na nivou godine, npr. 20210256)
		* **prosek** koji kao podrazumevanu vrednost ima 0
		* klasni atribut
			* **univerzitet** koji ima vrednost *Univerzitet umetnosti*

	* Napisati konstruktor za klasu.
	* Obezbediti metode za instance:
	* **formatiranIndeks** - koja vraća broj indeksa u obliku XXXX/GGGG
	* metod za predstavljanje objekta klase kao niske

	* Obezbediti klasni metod:

		* **kontakt** - koji kao rezultat vraća nisku koja sadrži naziv univerziteta i adresu univerziteta

	* Obezbediti statički metod:

		* **godinaIzIndeksa** - koji kao rezultat vraća godinu upisa na fakultet za studenta čiji je indeks prosleđen kao argument ovom metodu

	* [Resenje](./primer1.py)

# Nasleđivanje 
	

```python
	class BaznaKlasa:
	
		
		def __init__(self, arg1, arg2): 
		
			self.atribut1=arg1    
			self.atribut2=arg2
			
		def metod1(self, arg1, arg2, ..., argN):  #metod koji može da pozove instanca klase

			...
				      
				      
	class IzvedenaKlasa(BaznaKlasa):
		
		def __init__(self, arg1, arg2, arg3, arg4): 
		
			super().__init__(arg1,arg2)
			# ili
			# BaznaKlasa.__init__(self,arg1, arg2)
			
			self.atribut3=arg3    
			self.atribut4=arg4
			
	
		#metod roditeljske klase može biti redefinisan, ali ne mora
		def metod1(self, arg1, arg2, ..., argN):  
		...
			#bitno
				#u okviru metoda izvedene klase može se pozvati metod bazne klase sa
				#super().imeMetodaBazneKlase(arg1,arg2,...,argM)


		#metod specifičan za izvedenu klasu
		def metod2(self, arg1, arg2, ..., argN):  
		...

	
	objekat=IzvedenaKlasa(arg1V, arg2V,arg3V, arg4V)
	print(objekat.atribut1)
	print(objekat.atribut3)
	objekat.metod1()
	objekat.metod2()
	
```


2. Napraviti klasu 
	* **Osoba**
		* Od atributa klasa sadrži:
			* **ime**
			* **prezime**
			* **jmbg**
			* **kontakt**  koji sadrži broj telefona
		* Napisati konstruktor za klasu.
		* Obezbediti metode:
		* **datumRodjenja** - vraća datum rođenja u obliku DD.MM.GGGG.
		* metod za predstavljanje objekta klase kao niske

	* **Student** koja nasleđuje klasu **Osoba**
		* Od atributa klasa sadrži:
			* **indeks**  - zadaje se kao ceo broj  u obliku GGGGXXXX, gde je GGGG grodina upisa na fakultet, a XXXX jedinstven broj studenta na nivou godine, npr. 20210256)
			* **ispiti** - sadrži listu ispita studenta. Svaki element liste sadrži naziv predmeta koji je student polagao i ocenu koju je student dobio na ispitu.
	* Napisati konstruktor za klasu.
	* Obezbediti metode:

	* **formatiranIndeks** - vraća broj indeksa u obliku XXXX/GGGG
	* **dodajIspit** - u listu ispita dodaje podatak o novom ispitu koji je student polagao
	* **polozeniIspiti** - vraća nisku koja sadrži podatke o položenim ispitima
	* **prosek** - vraća prosečnu ocenu studenta dobijenu na položenim ispitima
	* metod za predstavljanje objekta klase kao niske

	* **Nastavnik** koja nasleđuje klasu **Osoba**
		* Od atributa klasa sadrži:
			* **zvanje**
			* **koeficijent**

	* Napisati konstruktor za klasu.
	* Obezbediti metode:

	* **plata** - vraća visinu plate nastavnika koja se računa prema izrazu koeficijent*3,5
	* metod za predstavljanje objekta klase kao niske



	* Napraviti
		* dva objekat klase **Osoba**
		* dva objekat klase **Student**
		* dva objekat klase **Nastavnik**
	i primeniti njihove metoda
	* [Resenje](./primer2.py)

3. Napraviti klasu **Pitanje** koja opisuje jedno pitanje u Kvizu. 
	* Od atributa klasa sadrži atribut za pitanje, po jedan atribut za 4 moguća odgovora i atribut za redni broj tačnog odgovora.
	* Napisati konstruktor za klasu.
	* Obezbediti metode:
	* **postaviPitanje** - ispisuje pitanje i moguće odgovore
	* **proveriOdgovor** - proverava da li je zadati odgovor tačan ili ne i vraća True ako jeste, a False ako nije.
	* Napraviti objekat klase **Pitanje**

	* Napraviti listu pitanja za kviz primenom klase **Pitanje** i simulirati kviz.
	* [Resenje](./primer3.py)

4. Napraviti klasu za kviz primenom klase **Pitanje** i simulirati kviz.
	* [Resenje](./primer4.py)

# Za vežbu

1. Napraviti klasu  **Prevodjenje**
	* koja od atributa za instance sadrži:
	 	* **prevodilac** - ime prevodioca
	 	* **oblast** - oblast na koju se odnosi prevod
		* **brojStrana** - broj prevedenih strana
		* **popust**  
	* koja od klasnih atributa sadrži:
	 	* **cenaPoStrani** - cena za prevođenje jedne strane iznosi 2000 RSD
	 
	* Napisati konstruktor za klasu.
	* Obezbediti metode:
	  * **povecajPopust**- povećava popust za zadatu vrednost
	  * **zaNaplatu** - vraća cenu prevoda uzimajući u obzir i popust
	  * metod za predstavljanje objekta klase kao niske

2. Napraviti klasu 
* **LikIzCrtanogFilma**
	* Od atributa sadrži:
	 	* **imeCrtanogFilma**
	 	* **karakter** - karakter lika može biti nepoznat, dobar ili loš
	 	
	* Napisati konstruktor za klasu.
	* Obezbediti metode:
	  * metod za predstavljanje objekta klase kao niske. Potrebno je da niska sadrži ime crtanog filma i opis karaktera.

* **Sirena** koja nasleđuje klasu **LikIzCrtanogFilma**
	* Od atributa  sadrži:
		* **ime**  	 	
		* **zeliDaPostaneCovek** - podatak da li sirena želi da postane čovek (True ili False) 
* Napisati konstruktor za klasu.
* Obezbediti metode:
  * metod za predstavljanje objekta klase kao niske.
Potrebno je da niska pored opisa lika sadrži i ime sirene i podataka da li sirena želi da postane čovek.

