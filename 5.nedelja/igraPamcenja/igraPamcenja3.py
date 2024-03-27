import pygame
from pygame.locals import *
import random

pygame.init()

background = (50, 201, 250)
message_color= (86, 11, 173)

screen = pygame.display.set_mode((500, 250))
screen.fill(background)
pygame.display.set_caption("Igra pamcenja")

font = pygame.font.SysFont("Viga", 30)

class Cell:
    text_color=(247, 37, 133)
    background_color = (72, 149, 239)
    cell_font = pygame.font.SysFont("Viga", 50)
    box_size = 50 #dodavanje stranice polja

    def __init__(self, topLeft, value=0):
        self.value=value
        self.guessed = False
        self.image = self.cell_font.render(' * ', True, self.text_color)

        #pravljenje povrsine u koju ce se dodati slika teksta
        self.surface = pygame.Surface((self.box_size,self.box_size))
        self.surface.fill(self.background_color) #postavljenje pozadine povrsine

        #smestanje slike na sredinu povrsine
        self.surface.blit(self.image, ((self.box_size-self.image.get_width())/2,
                                       (self.box_size - self.image.get_height())/2))

        #odredjivanje pravugaonika povrsine i postavljanje gornjeg levog ugla
        self.rect = self.surface.get_rect(topleft=topLeft)

    def showValue(self, yes=False):
        if yes or self.guessed:
            self.image = self.cell_font.render(f" {self.value} ", True, self.text_color)
        else:
            self.image = self.cell_font.render('*', True, self.text_color)

        #azuriranje povrsine u koju se smesta slika
        self.surface.fill(self.background_color)
        self.surface.blit(self.image, ((self.box_size-self.image.get_width())/2,
                                       (self.box_size - self.image.get_height())/2))

running = True

values = list(range(1, 9))
values += values

cells = []
for i in range(0, 4):
    for j in range(0, 4):
        x = random.randint(0, len(values) - 1)
        cells.append(Cell((10+i * 60, 10+j * 60), values[x]))
        del values[x]
        screen.blit(cells[-1].surface, cells[-1].rect)

num_of_pairs = 0
value_of_clicked_cells=[]

num_of_pairs_mess=font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
screen.blit(num_of_pairs_mess, (300,10))


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONUP:
            screen.fill(background)
            pos = pygame.mouse.get_pos()

            for ind in range(0, len(cells)):
                if cells[ind].rect.collidepoint(pos) and \
                                ind not in value_of_clicked_cells:
                    value_of_clicked_cells.append(ind)

            for ind in range(0, len(cells)):
                if ind in value_of_clicked_cells:
                    print(ind)
                    cells[ind].showValue(True)

                #umesto slike iscrtava se povrsina u koju je smestena slika
                #vezana za polje
                screen.blit(cells[ind].surface, cells[ind].rect)

            pygame.display.update()

            if len(value_of_clicked_cells)==2:
                screen.fill(background)

                num_of_pairs+=1
                pygame.time.wait(1000)
                if cells[value_of_clicked_cells[0]].value == cells[value_of_clicked_cells[1]].value:
                    cells[value_of_clicked_cells[0]].guessed = True
                    cells[value_of_clicked_cells[1]].guessed = True

                    #provera kraja
                    end=True
                    for cell in cells:
                        if cell.guessed == False:
                            end=False

                    if end:
                        message= font.render("Čestitamo!", True, message_color)
                        screen.blit(message, (300, 50))
                        running=False

                for cell in cells:
                    cell.showValue(False)
                    # umesto slike iscrtava se povrsina u koju je smestena slika
                    # vezana za polje
                    screen.blit(cell.surface, cell.rect)
                value_of_clicked_cells = []

            num_of_pairs_mess = font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
            screen.blit(num_of_pairs_mess, (300, 10))

    pygame.display.update()

pygame.time.wait(1000)
pygame.quit()
