import pygame
from pygame.locals import  K_UP,K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT
import random

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_COLOR = (255,255,255)
MESS_COLOR = (0, 255, 0)

#klasa za igraca
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2,0)

        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right>SCREEN_WIDTH:
            self.rect.right=SCREEN_WIDTH
        if self.rect.top <0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#klasa za slova
class Letter(pygame.sprite.Sprite):

    #atributi klase
    font = pygame.font.SysFont("Comic Sans", 50)
    color = (0,0,255)

    def __init__(self, value):
        super().__init__()

        self.value = value
        self.image = self.font.render(self.value, True, self.color)
        self.rect = self.image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH-self.image.get_width()),
                                                 random.randint(0, SCREEN_HEIGHT - self.image.get_height())))

#pravljenje prozora
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(SCREEN_COLOR)
pygame.display.set_caption("Slova")

running = True

all_sprites = pygame.sprite.Group()
all_letters = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for l in  "umetnost":
    letter = Letter(l)
    all_sprites.add(letter)
    all_letters.add(letter)

font = pygame.font.SysFont("Comic Sans", 35)
num = 0

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    #azuriranje pozicije igraca prema pritisnutim tasterima
    player.update(pygame.key.get_pressed())

    #odredjivanje svih slova koji su u koliziji sa igracem i njihovo brisanje
    successful_letters = pygame.sprite.spritecollide(player, all_letters, True)

    #povecavanje broja pokupljenih slova
    num+=len(successful_letters)

    #novo iscrtavanje
    screen.fill((255, 255,255))
    all_sprites.draw(screen)

    #formiranje poruke
    if num == len("umetnost"):
        text = font.render("Bravo!", True, MESS_COLOR)
        running = False
    else:
        text = font.render(f"Broj pogodaka {num}", True, MESS_COLOR)

    #prikaz poruke u donjem desnom uglu
    screen.blit(text, text.get_rect(bottomright=(SCREEN_WIDTH,SCREEN_HEIGHT)))

    pygame.time.wait(20)

    #azuriranje prozora
    pygame.display.update()

pygame.time.wait(2000)
pygame.quit()
