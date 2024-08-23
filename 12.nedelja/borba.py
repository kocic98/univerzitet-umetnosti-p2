import pygame
import random

pygame.init()

velicina_prozora = (800,600)
font = pygame.font.SysFont("",40)
ekran = pygame.display.set_mode(velicina_prozora)
boja_pozadine = "white"
running = True
sat = pygame.time.Clock()

class objekat(pygame.sprite.Sprite):
    def __init__(self,tip) -> None:
        super().__init__()
        self.tip = tip
        self.image = pygame.Surface((50,50))
        self.image.fill("black")
        if tip == 'kamen':
            self.image = pygame.image.load('kamen.png')
        elif tip == 'makaze':
            self.image = pygame.image.load("makaze.png")
        else:
            self.image = pygame.image.load('papir.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        
        x = random.randint(0,velicina_prozora[1]-50)
        y = random.randint(0,velicina_prozora[0]-50)
        self.rect = self.image.get_rect(topleft=(x,y))
        a = random.randint(1,3)
        self.speed = (a,3-a)
    def promeni_sliku(self,slika):
        self.image= pygame.image.load(slika)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey("white")
        self.image.convert_alpha()
        self.promeni_smer()
    def promeni_smer(self):
        self.speed = (-self.speed[0],-self.speed[1])
    def update(self):
        a = random.randint(1,5)
        if self.rect.bottom >= velicina_prozora[1]:
            self.speed = (self.speed[0],-a)
            self.rect.bottom = velicina_prozora[1]
        if self.rect.right >= velicina_prozora[0]:
            self.speed = (-a,self.speed[1])
            self.rect.right = velicina_prozora[0]
        if self.rect.left <= 0:
            self.speed = (a,self.speed[1])
            self.rect.left = 0
        if self.rect.top <= 0:
            self.speed = (self.speed[0],a)
            self.rect.top = 0
        self.rect.move_ip(self.speed)
    def kill(self):
        pass


    
makaze = pygame.sprite.Group()
papir = pygame.sprite.Group()
kamen = pygame.sprite.Group()
svi = pygame.sprite.Group()
for i in range(10):
    makaze.add(objekat('makaze'))
    papir.add(objekat("papir"))
    kamen.add(objekat("kamen"))

for i in kamen.sprites():
    svi.add(i)
for i in makaze.sprites():
    svi.add(i)
for i in papir.sprites():
    svi.add(i)
pobednik = pygame.image.load("kamen.png")
while running:
    ekran.fill(boja_pozadine)
    # sad = pygame.image.load('kamen.png')
    # ekran.blit(sad,(0,0))
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    svi.update()
    svi.draw(ekran)
    for i in kamen:
        if pygame.sprite.spritecollide(i,papir,False):
            kamen.remove(i)
            i.promeni_sliku("papir.png")
            papir.add(i)
    for i in papir:
        if pygame.sprite.spritecollide(i,makaze,False):
            papir.remove(i)
            i.promeni_sliku("makaze.png")
            makaze.add(i)
        
    for i in makaze:
        if pygame.sprite.spritecollide(i,kamen,False):
            makaze.remove(i)
            i.promeni_sliku("kamen.png")
            kamen.add(i)
    
    # pygame.sprite.groupcollide(kamen,makaze,False,True)
    # pygame.sprite.groupcollide(makaze,papir,False,True)
    # pygame.sprite.groupcollide(papir,kamen,False,True)
    if len(kamen.sprites())==0:
        pobednik = pygame.image.load("makaze.png")
        running = False
    elif len(makaze.sprites())==0:
        pobednik = pygame.image.load("papir.png")
        running = False
    elif len(papir.sprites())==0:
        running = False

    pygame.display.update()
    sat.tick(20)

ekran.fill(boja_pozadine)
ekran.blit(pobednik,(200,150))
text = font.render("Pobedio je:",False,"black")
ekran.blit(text,(0,200))
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()