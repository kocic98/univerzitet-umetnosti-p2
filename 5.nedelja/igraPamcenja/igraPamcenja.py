import pygame #ucitavanje biblioteke pygame
from pygame.locals import *
import random

pygame.init() #inicijalizacija modula

"""
Izgled prozora
----------------------------------
*  5  *  *      Broj pokusaja: Y
*  *  *  *
*  *  5  *
*  *  *  *
----------------------------------
"""

#postavljanje boja
background = (50, 201, 250)
message_color= (86, 11, 173)

#pravljenje prozora
screen = pygame.display.set_mode((500, 250))
screen.fill(background)
pygame.display.set_caption("Igra pamcenja")

#postavljanje fonta koji ce biti koriscen za prikaz teksta
font = pygame.font.SysFont("Viga", 25)

#klasa koja predstavlja jedno polje sa brojem
#u tabeli za pogadjanje parova

class Cell:
    #postavljanje boja za polja
    text_color=(247, 37, 133)
    background_color = (72, 149, 239)

    # postavljanje fonta koji ce biti koriscen za prikaz brojeva
    cell_font = pygame.font.SysFont("Viga", 50)

    def __init__(self, topLeft, value=0):
        self.value=value  #broj koji je vezan za polje
        self.guessed = False    #podatak da li je par za vezani broj pogodjen

        #pravljenje slike sa tekstom koji ce inicijalno biti prikazan (*)
        self.image = self.cell_font.render('*', True, self.text_color,
                                           self.background_color)

        # definisanje pozicije polja na tabeli za pogadjanje
        self.rect = pygame.Rect(topLeft,(50,50))

    #metod kojim se odredjuje sta ce biti prikazano na polju
    def showValue(self, yes=False):
        #ako se trazi prikaz broja ili je pogodjen broj koji je vezan za polje,
        #prikazuje se broj
        if yes or self.guessed:
            self.image = self.cell_font.render(str(self.value), True, self.text_color, self.background_color)
        #u suprotnom se prikazuje *
        else:
            self.image = self.cell_font.render('*', True, self.text_color, self.background_color)


running = True #promenljiva za petlju igre

#vrednosti koje se koriste za dodelju brojeva poljima
values = list(range(1, 9))  # pravi se lista [1,2,3,4,5,6,7,8]
values += values   #dupliraju se elementi liste

#pravljenje polja u tabeli za pogadjanje
cells = []  #lista napravljenih polja
for i in range(0, 4):
    for j in range(0, 4):
        x = random.randint(0, len(values) - 1) #bira se nasumicno indeks iz liste values
        #pravi se polje za koje se vezuje broj sa izvucenim indeksom
        cells.append(Cell((10+i * 60, 10+j * 60), values[x]))

        del values[x]  #izvuceni broj se brise iz liste

        #dodaje se polje na ekran
        screen.blit(cells[-1].image, cells[-1].rect)

num_of_pairs = 0  # promenljiva za broj parova
# lista koja ce sadrzati informacije o izabranim parovima za tekuci pokusaj
value_of_clicked_cells = []

#pravi se slika za tekst sa porukom o broju zadatih parova
num_of_pairs_mess=font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
screen.blit(num_of_pairs_mess, (300,0))

#pygame.display.update()

#petlja igre (tj. glavna petlja)
while running:

    #obrada dogadjaja
    for event in pygame.event.get():

        if event.type == QUIT:   #provera da li je kliknuto na dugme za zatvaranje prozora
            running = False  #daje se signal za prekid glavne petlje

        #za prvi deo, radi provere da li showValue radi dobro
        if event.type == KEYDOWN:
            screen.fill(background)
            for cell in cells:
                cell.showValue(True)
                screen.blit(cell.image,cell.rect)

            num_of_pairs_mess = font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
            screen.blit(num_of_pairs_mess, (300, 0))

        #------------------------------------------------------

        # provera da li je klinuto misem
        if event.type == MOUSEBUTTONUP:

            screen.fill(background)  #postavljanje pozadine radi novog iscrtavanja
            pos = pygame.mouse.get_pos() #uzima se pozicija na kojoj je kliknuto

            #trazi se polje na koje je kliknuto i njegov indeks se dodaje
            #u listu izabranih polja
            for ind in range(0, len(cells)):
                if cells[ind].rect.collidepoint(pos) and \
                                ind not in value_of_clicked_cells:
                    value_of_clicked_cells.append(ind)

            #prikaza brojeva za izabrana polja
            for ind in range(0, len(cells)):
                if ind in value_of_clicked_cells:
                    cells[ind].showValue(True)

                #dodavanje polja na ekran
                screen.blit(cells[ind].image, cells[ind].rect)

            pygame.display.update() #azuriranje prikaza

            #obrada situacije kada se izabrana dva polja
            if len(value_of_clicked_cells)==2:
                screen.fill(background)  #postavljanje boje pozadine

                num_of_pairs+=1  #povecava se broj izabranih parova
                pygame.time.wait(1000) #cekanje radi duzeg prikaza izbora

                #obrada slucaja kada je par pogodjen
                if cells[value_of_clicked_cells[0]].value == cells[value_of_clicked_cells[1]].value:
                    #u poljima se oznacava da je par broja pogodjen
                    cells[value_of_clicked_cells[0]].guessed = True
                    cells[value_of_clicked_cells[1]].guessed = True

                    #provera da li su pogodjeni svi parovi
                    end=True  #promenljiva koja oznacava da jesu pogodjeni svi parovi
                    for cell in cells:
                        if cell.guessed == False:
                            end=False
                            break

                    if end:
                        #prikaz poruke za cestitanje
                        message= font.render("Čestitamo!", True, message_color)
                        screen.blit(message, (300, 50))
                        running=False

                #prikaz stanja nakon obrade izabranog para
                #tj. prikazuju se samo pogodjeni parovi
                for cell in cells:
                    cell.showValue(False)
                    screen.blit(cell.image, cell.rect)

                #praznjenje liste izabranih parova
                value_of_clicked_cells = []

            #osvezavanje poruke sa brojem pokusaja
            num_of_pairs_mess = font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
            screen.blit(num_of_pairs_mess, (300, 0))

    pygame.display.update()#azuriranje ekrana

pygame.time.wait(1000) #kratko cekanje pre zatvaranja ekrana
pygame.quit()
