import pygame #ucitavanje biblioteke pygame
from pygame.locals import *
import random

pygame.init()

background = (50, 201, 250)
message_color= (86, 11, 173)

screen = pygame.display.set_mode((500, 250))
screen.fill(background)
pygame.display.set_caption("Igra pamcenja")

font = pygame.font.SysFont("Viga", 25)

#razlika u odnosu na prethodnu verziju - dodavanje blanko pre i posle ispisa
#* ili broja da bi se dobilo sire polje
class Cell:
    text_color=(247, 37, 133)
    background_color = (72, 149, 239)
    cell_font = pygame.font.SysFont("Viga", 50)

    def __init__(self, topLeft, value=0):
        self.value=value
        self.guessed = False
        self.image = self.cell_font.render(' * ', True, self.text_color, self.background_color)
        self.rect = pygame.Rect(topLeft,(50,50))

    def showValue(self, yes=False):
        if yes or self.guessed:
            self.image = self.cell_font.render(f" {self.value} ", True, self.text_color, self.background_color)
        else:
            self.image = self.cell_font.render(' * ', True, self.text_color, self.background_color)


running = True

values = list(range(1, 9))
values += values

cells = []
for i in range(0, 4):
    for j in range(0, 4):
        x = random.randint(0, len(values) - 1)
        cells.append(Cell((10+i * 60, 10+j * 60), values[x]))
        del values[x]
        screen.blit(cells[-1].image, cells[-1].rect)

num_of_pairs = 0
value_of_clicked_cells=[]

num_of_pairs_mess=font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color, (0,255,0))
screen.blit(num_of_pairs_mess, (300,0))

pygame.display.update()

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            screen.fill(background)
            for cell in cells:
                cell.showValue(True)
                screen.blit(cell.image,cell.rect)

            num_of_pairs_mess = font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
            screen.blit(num_of_pairs_mess, (300, 0))

        if event.type == MOUSEBUTTONUP:
            screen.fill(background)
            pos = pygame.mouse.get_pos()

            for ind in range(0, len(cells)):
                if cells[ind].rect.collidepoint(pos) and \
                                ind not in value_of_clicked_cells:
                    value_of_clicked_cells.append(ind)

            for ind in range(0, len(cells)):
                if ind in value_of_clicked_cells:
                    cells[ind].showValue(True)

                screen.blit(cells[ind].image, cells[ind].rect)

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
                            break

                    if end:
                        message= font.render("Čestitamo!", True, message_color)
                        screen.blit(message, (300, 50))
                        running=False

                for cell in cells:
                    cell.showValue(False)
                    screen.blit(cell.image, cell.rect)
                value_of_clicked_cells = []

            num_of_pairs_mess = font.render(f"Broj pokušaja: {num_of_pairs}", True, message_color)
            screen.blit(num_of_pairs_mess, (300, 0))

    pygame.display.update()

pygame.time.wait(1000)
pygame.quit()
