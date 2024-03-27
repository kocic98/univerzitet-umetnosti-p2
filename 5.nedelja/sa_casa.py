import pygame
import random
pygame.init()


velicina_prozora=(400,300)
ekran = pygame.display.set_mode(velicina_prozora)
pygame.display.set_caption("Memorija")

ekran.fill("lightblue")

font = pygame.font.SysFont("Arial", 40)
class polje:
    font = pygame.font.SysFont("Arial", 50)
    def __init__(self,vrednost,mesto) -> None:
        self.vrednost = vrednost
        self.mesto = mesto
        self.resen = False
        # self.slika  = self.font.render("*", False,"white","blue")
        self.pravougaonik = self.iscrtaj().get_rect(topleft = mesto)
    def iscrtaj(self,provera = False):
        if self.resen:
            return self.font.render("", False,"white","blue")
        if provera == False:
            return self.font.render("*", False,"white","blue")
        if provera == True:
            return self.font.render(str(self.vrednost),False,"white","blue")
    def kliknuo(self, mesto):
        if self.resen:
            return False
        if self.pravougaonik.collidepoint(mesto):
            return True
        return False
brojevi = list(range(1,9))

brojevi += brojevi
random.shuffle(brojevi)


polja = []
par = []
brojac = 0
for i in range(4):
    for j in range(4):
        polja.append(polje(brojevi[brojac], (10+ j * 60, 10+ i * 60)))
        brojac += 1

dozvoljeno = 50
def crtaj():
    ekran.fill("lightblue")
    for p in polja:
        ekran.blit(p.iscrtaj(),p.pravougaonik)
    for i in par:
        ekran.blit(polja[i].iscrtaj(True), polja[i].pravougaonik)
    poeni = font.render(str(dozvoljeno),False,"darkgreen")
    ekran.blit(poeni,(320,10))
crtaj()


running = True
while running:
    if len(par) == 2:
        pygame.time.wait(1000)
        if polja[par[0]].vrednost == polja[par[1]].vrednost:
            polja[par[0]].resen = True
            polja[par[1]].resen = True
            dozvoljeno += 5
        par.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(polja)):
                if polja[i].kliknuo(pygame.mouse.get_pos()) and i not in par:
                    par.append(i);
                    dozvoljeno -= 1
    if dozvoljeno == 0:
        go = font.render("Game over!",False, "red")
        ekran.fill("lightblue")
        ekran.blit(go, (150,120))
    else:
        crtaj()
    pygame.display.update()
    
pygame.quit()