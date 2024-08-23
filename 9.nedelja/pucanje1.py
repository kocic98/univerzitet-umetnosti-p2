import pygame
import random

#ucitavanje imenovanih konstanti za tastere koji ce biti korisceni
from pygame.locals import  K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_s

#postavljanje sirine i visine prozora
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#klasa kora predstavlja korisnika
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('fighter.png').convert()
        self.rect = self.image.get_rect()

    #metod za auziranje stanja igraca
    def update(self, pressed_keys):

        #pomeranje igraca prema pritisnutim tasterima
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2,0)

        #provera da li igrac izlazi van prozora
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right>SCREEN_WIDTH:
            self.rect.right=SCREEN_WIDTH
        if self.rect.top <0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    #metod za ispaljivanje metka
    def shoot(self):
        return Bullet((self.rect.right, random.randint(self.rect.top, self.rect.bottom)))
                #inicijalna pozicija levog gornjeg ugla se odredjuje prema pravilu:
                    # x koordinata metka uzima vrednost koju ima desna ivica aviona
                    # y koordinata metka uzima vrednost koja je izmedju gorinje i
                    # donje ivice aviona

#klasa koja predstavlja metak
class Bullet(pygame.sprite.Sprite):

    def __init__(self, position):  #konstruktoru se prosledjuje inicijalna pozicija metka
        super().__init__()
        self.image = pygame.image.load('bullet.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center = position)
        self.speed = random.randint(5,20) #odredjivanje brzine kretanja

    #metod za azuriranje stanja metka
    def update(self):
        self.rect.move_ip(self.speed, 0) #pomeranje metka
        if self.rect.left>SCREEN_WIDTH: #brisanje metka kada predje desnu ivicu prozora
            self.kill()

pygame.init() #inicijalizacija modula

#pravljenje prozora
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#pravljenje igraca - aviona
player = Player()

#pravljenje grupe koja ce sadrzati sve metkice
bullets = pygame.sprite.Group()
#pravljenje grupe koja ce sadrzati sve sprajtove
all_sprites = pygame.sprite.Group()

#dodavanje igraca u grupu
all_sprites.add(player)

#pravljenje zvuka
sound = pygame.mixer.Sound("zvuk.mp3")

#promenljiva za glavnu petlju
running = True

#petlja igre (tj. glavna petlja)
while running:

    #obrada dogadjaja
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            #obrada naredbe za pucanje
            if event.key == K_s:
                bullet = player.shoot() #pravljenje metka
                all_sprites.add(bullet) #dodavanje novog metka u grupu sa svim sprajtovima
                bullets.add(bullet) #dodavanje novog metka u grupu sa svim metkicima
                sound.play() #pustanje zvuka

        elif event.type == QUIT:
            running = False


    #svi pritisnuti tasteri
    pressed_keys = pygame.key.get_pressed()

    #azuriranje aviona i metkica
    player.update(pressed_keys)
    bullets.update()

    #bojenje prozora
    screen.fill((255, 255,255))

    #iscrtavanje svih sprajtova
    all_sprites.draw(screen)

    #azuriranje prozora
    pygame.display.update()
    #cekanje 20 milisekundi
    pygame.time.wait(20)

#cekanje sekund pre kraja
pygame.time.wait(1000)
pygame.quit()