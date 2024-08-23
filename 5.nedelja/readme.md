# Pygame


```
import pygame #uvoz biblioteke

pygame.init()  

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 60

#pravljenje prozora igrice
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
screen.fill((255,255,255))  
pygame.display.set_caption("Uvodni primer")

pygame.display.update()

#cekanje odredjenog vremena pre zatvaranja prozora
pygame.time.wait(5000) 

pygame.quit()


```
	
## Bitne funkcije

* pygame.init() - inicijalizacija modula
* pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) - inicijalizacija prozora za prikazivanje i zadavanje veličine istog
* screen.fill(color) - postavljanje boje pozadine
* pygame.display.set_caption(text) - postavljanje naslova prozora
* pygame.display.update() - ažuriranje prozora
* pygame.quit() -  oslobađa sve pygame module


## Priкaz teksta

* modul: pygame.font
* font.SysFont(name, size, bold=False, italic=False) - pravi objekat klase Font korišćenjem sistemskih fontova 
* Font.render(text, antialias, color, background=None) - prikaz teksta na površini (Surface)
	* ako je antialias postavljen na True, karakteri će imati glatke ivice


## Površine (Surface)

* objekat za predstavljanje slika
* Surface.blit(source, dest) 
  * crta jednu površinu (source) u površinu koja je pozvala metod
  * dest je gornji levi ugao pravugaonika u koji će biti iscrtana prosleđena površina
* Surface.set_colorkey(color) - pikseli površine sa zadatom bojom će biti transparentni
* Surface.get_width() - vraća širinu površine
* Surface.get_height() - vraća visinu površine
* Surface.get_rect() - vraća pridruženi pravugaonik	
	* vraća objekat klase Rect

## Pravugaonik (Rect)

* objekat za čuvanje koordinata pravugaonika
	* Rect(left, top, width, height) 
 	* Rect((left, top), (width, height)) 
* pygame koristi Rect objekte za čuvanje i manipulaciju pravugaonih oblasti 
* neki od atributi koji mogu da se koriste radi pomeranja   
 	* topleft, bottomleft, topright, bottomright
 	* center, centerx, centery
 	* size, width, height
* Rect.collidepoint(x, y) - proverava da li je zadata tačka u pravugaoniku 
 	* vraća vrednost tipa bool


## Obrada događaja 

* Događaji - pomeranje miša, pritisak na dugme miša ili tastera na tastaturi 
* modul: pygame.event
* pygame.event.get() - red događaja
* potrebno je u kodu obezbediti i obradu različitih događaja (event handler)
* Svaki događaj ima pridruženi tip (type)  
	* pritisak tastera pripada tipu KEYDOWN
	* zatvaranje prozora tipu QUIT
	* otpuštanje dugmića na mišu ima tip MOUSEBUTTONUP 
* Svaki tip može imati i dodatne pridružene podatke, npr. KEYDOWN ima pridruženu promenljivu *key* koja sadrži informaciju koji taster je pridružen. 
	* pygame.locals - sadrži imenovane konstante za svaki  taster. Može im se pristupiti sa pygame.*CONSTANT*  ili se uključuju preko modula locals i pozivaju sa *CONSTANT* (npr. K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_b)
* pygame.mouse - modul za rad sa mišem
	* mouse.get_pos() - vraća uređeni par koordinata na kojoj se trenutno nalazi pokazivač miša. 
* pygame.key - modul za rad sa tastaturom
	* key.get_pressed() - vraća torku elemenata čiji se elementi koriste kao logičke vrednosti koje pokazuju da li je određeni taster pritisnut ili nije 
* event.unicode - atribut koji sadrži karaker koji je pridružen pritisnutom tasteru


## Petlja igrice

```
running = True

while running:
	...
	
```
* Za kontrolu igirce koristi se petlja. Petlja igrice radi sledeće
	* obrađuje ulaz korisnika
	* ažurira stanje svih objekata igrice
	* ažurira prikaz i audio izlaz
	* upravlja brzinom igrice
* Svaki ciklus u petlji igrice je frejm. 
* Frejmovi se smenjuju dok se ne ispuni neki uslov za kraj igrice.

## Zadatak 
1. Napraviti igru **Pamćenje** u kojoj korisnik traži kartice sa istim brojevima. Potrebno je da prozor igrice izgleda kao na slici. Obezbediti sledeće funkcionalnosti u igrici:
* Na ekranu se prikazuje tabela veličine 4x4. 
* Za svako polje je vezan jedan broj. 
* Inicijalno su sva polja tabele *zatvorena*, tj. umesto njihovih brojeva prikazuje se karakter *.
* Cilj je pronaći polja, tj. par sa istim brojem.
* Korisnik bira po dva polja. 
* Kada se klikne na polje  prikazuje se dodeljen broj.
* Ukoliko su izabrana polja sa istim brojem, polja se *otvaraju*, tj. par je pogođen i u ostatku igre ostaju prikazani brojevi tih polja. Ukoliko su izabrana polja sa različitim brojevima, polja se opet *zatvaraju* .
* Prikazuje se tekst sa brojem parova koje je korisnik zadao.
*   Kada korisnik klikne na dugme za zatvaranje prozora, prozor se zatvara.
*  Kada korisnik pronađe sve parove brojeva na prozoru se ispisuje poruka *Čestitamo!*

![image](./primer1.png)


 ## Iscrtavanje geometrijskih objekata
* modul: pygame.draw
* draw.rect(surface, color, rect, width=0) - iscrtava pravugaonik
	* width=0 označava da se pravugaonik popunjava bojom. Ako je width>1 onda se crta samo ivica, a zadata vrednost predstavlja njenu debljinu
* draw.circle(surface, color, center, radius, width=0) - iscrtava krug
* draw.arc(surface, color, rect, start_angle, stop_angle) - iscrtava luk	

## Zadatak

2. Proširiti igricu *Vešanje* sa prethodnog časa dodavanjem ograničenja da korisnik može da unese do 10 pogrešnih karaktera i obezbediti prikaz po jednog dela tela čikice za svaki zadati karakter koji se ne nalazi u reči za pogađanje.
Redosled prikaza delova tela je: oblik glave, levo oko, desno oko, nos, usta, telo, leva ruka, desna ruka, leva noga, desna noga.

![image](./primer4.png)


