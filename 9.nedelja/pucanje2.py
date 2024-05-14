import pygame
import random

from pygame.locals import  K_UP,K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_s

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('fighter.png').convert()
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

    def shoot(self):
        return Bullet((self.rect.right, random.randint(self.rect.top, self.rect.bottom)))


class Bullet(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('bullet.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center = position)
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left>SCREEN_WIDTH:
            self.kill()

#klasa koja predstavlja cilj koji je potrebno unistiti
class Target(pygame.sprite.Sprite):

    size = 150  #velicina kvadrata

    def __init__(self):
        super().__init__()
        self.color_value=0 # vrednost za R i G boje
        #pravljanje kvadrata
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((self.color_value, self.color_value, 255))
        #nasumicno odredjivanje pozicije kvadrata uz desnu ivicu prozora
        self.rect = self.image.get_rect( topleft = (SCREEN_WIDTH-self.size, (random.randint(0,SCREEN_HEIGHT-self.size))))

    #azuriranje stanja (boje) kvadrata
    def update(self, shoot=False):

        #ako je cilj pogodjen i jos nije bele boje
        if shoot and self.color_value <255:
            self.color_value += 5  #povecava se vrednost za R i G komponente
            self.image.fill((self.color_value, self.color_value, 255))
            if self.color_value == 255: #ako je kvadrat bele boje zavrsava se igrica
                pygame.quit()
                quit()

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player = Player()
target = Target()  #pravljenje cilja

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(target) #dodavanje cilja u grupu sa sprajtovima

sound = pygame.mixer.Sound("zvuk.mp3")

running = True


while running:

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            if event.key == K_s:
                bullet = player.shoot()
                all_sprites.add(bullet)
                bullets.add(bullet)
                sound.play()

        elif event.type == QUIT:
            running = False


    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    bullets.update()

    screen.fill((255, 255,255))


    #odredjivanje svih metkica koji su u koliziji sa ciljem
    successful_bulets = pygame.sprite.spritecollide(target, bullets, True)

    #azuriranje stanja cilja na osnovu metkica koji su ga pogodili
    for sb in successful_bulets:
        target.update(True)

    all_sprites.draw(screen)

    pygame.display.update()
    pygame.time.wait(20)

pygame.time.wait(1000)
pygame.quit()