# Klase i nasleđivanje
	
1. Napraviti klasu **Racun** koja opisuje dinarski račun u banci.
	* Od atributa sadrži:
		* atribute koji opisuju instance
		 	* **id**
		 	* **vlasnik**
			* **stanje**  
				
		* klasni atribut
			* **kursnaLista** koji sadrži vrednost 1 RSD u različitim valutama
			 
	* Napisati konstruktor za klasu.
	* Obezbediti metode za instance:
	  * **dodaj** koji dodaje zadatu količinu RSD na račun
	  * **skini** koji oduzima zadatu količinu RSD sa računa ukoliko ima sredstava. Ukoliko na računu nema sredstava ispisuje odgovarajuću poruku. Ukoliko je akcija uspešno izvršena metod vraća vrednost True, a u suprotnom False.
	  * **prenesi** koji sa računa koji je pozvao metod prenosi zadatu količinu RSD na željeni račun. Ukoliko na računu nema sredstava ispisuje odgovarajuću poruku.
	  * metod za predstavljanje objekta klase kao niske
	
	* Obezbediti klasni metod:
	
		* **konvertuj** koji vrši konverziju zadate sume u RSD u željenu valutu i izračunatu vrednost vraća kao rezultat.  
	


2. Napraviti klasu 
* **Predstava**
	* Od atributa klasa sadrži:
	 	* **naziv**
	 	* **premijera** - datum premijere
		* **reditelj** 
		* **izvodjaci**  - sadrži listu izvođača 
	* Napisati konstruktor za klasu.
	* Obezbediti metode:
	  * **dodajIzvodjaca** 
	  * **ispisiIzvodjace**
	  * metod za predstavljanje objekta klase kao niske

* **Drama** koja nasleđuje klasu **Predstava**
	* Od atributa klasa sadrži:
		* **pisac**  
		* **dramaturg** 
	* Napisati konstruktor za klasu.
	* Obezbediti metod za predstavljanje objekta klase kao niske.


* **Opera** koja nasleđuje klasu **Predstava**
	* Od atributa klasa sadrži:
		* **kompozitor**  
		* **dirigent** 
	* Napisati konstruktor za klasu.
	* Obezbediti metod za predstavljanje objekta klase kao niske.




3. Napraviti klasе koje su potrebne za online kupovinu karata.
Napraviti klase:

	 * **Karta** koja opisuje jednu kupljenu kartu. 
		 * Od atributa sadrži:
			* atribute koji opisuju instance
			 	* **predstava**
			 	* **oznaka** - oznaka sedišta
				* **vreme**
				* **kategorija** - kategorija sedišta
					
			* klasni atribut
				* **kаtegorije** koji za svaku kategoriju sadrži cenu za mesta iz te kategorije
				 
		* Napisati konstruktor za klasu.
		* Obezbediti metod za instance:
		  * **cena** koji vraća cenu karte
		  * metod za predstavljanje objekta klase kao niske
		
	 * **Kupovina** koja opisuje jednu transakciju. 
		 * Od atributa koji opisuju instance sadrži:
	
			 * **karte** - lista kupljenih karata 
			 	 
		* Napisati konstruktor za klasu.
		* Obezbediti metod za instance:
		  * **dodajKartu** koji dodaje novu kartu u listu karata kupljenih u okviru transakcije
		  * **ukupnoZaNaplatu** koji računa i vraća ukupnu cenu kupljenih karata. Kao argument se može zadati i popust koji se uzima u obzir prilikom računanja cene. Vrednost popusta je  u intervalu [0,1). Podrazumevano je da nema popusta, tj. iznosi 0. 
		 
		  * metod za predstavljanje objekta klase kao niske
	
	 * **Klijent** koja opisuje jednog klijenta i čuva podatke o njegovim transakcijama
	
		 * Od atributa sadrži:
			* atribute koji opisuju instance
			 	* **ime**
			 	* **kontakt** 
				* **tip** - moguće vrednosti su zlatni, srebrni i bronzani
				* **kupovine** - lista obavljenih kupovina, tj. transakcija
					
			* klasni atribut
				* **tipovi** koji za svaki tip klijenta sadrži informaciju o popustu koji ostvaruju pri kupovini
				 
		* Napisati konstruktor za klasu.
		* Obezbediti metod za instance:
		  * **dodajKupovinu** koji u listu kupovina dodaje novu kupovinu 
		  * metod za pristup određenoj kupovini preko njenog indeksa
		
		  * metod za predstavljanje objekta klase kao niske
		


