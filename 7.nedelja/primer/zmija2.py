
import pygame
import time
from random import randint

SPEED_DELAY = 0.1
STEP_SIZE = 20
BG_COLOR = (0,0,0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Igra Zmijica")

running = True

class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_seg.gif")
        self.rect = self.image.get_rect()
        self.direction =  DOWN

    def update(self):

        if self.direction == UP:
            self.rect.top -= STEP_SIZE

        elif self.direction == DOWN:
            self.rect.top += STEP_SIZE

        elif self.direction == LEFT:
            self.rect.left -= STEP_SIZE

        elif self.direction == RIGHT:
            self.rect.left += STEP_SIZE

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

#klasa koja predstavlja jabuku
class Apple(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.gif") #pravljenje slike jabuke
        self.rect = self.image.get_rect() #pravljenje pridruzenog  pravugaonika
        self.live = False # oznaka da li se prikazuje jabuka

    #metod za azuriranje stanja (tj. pozicije) jabuke
    def update(self):
        #ako se ne prikazuje jabuka, nasumicno joj se odredjuje polozaj
        #i postavlja oznaka live na True da bi se jabuka prikazala na prozoru
        if not self.live:
            self.rect.top = randint(0, SCREEN_HEIGHT - STEP_SIZE)
            self.rect.top -= self.rect.top % STEP_SIZE  # zbog uslova da vrednosti pozicija budu deljive sa STEP_SIZE
            self.rect.left = randint(0, SCREEN_WIDTH - STEP_SIZE)
            self.rect.left -= self.rect.left % STEP_SIZE # zbog uslova da vrednosti pozicija budu deljive sa STEP_SIZE
            self.live = True

snake=Snake()

#pravljenje objekta koji predsstavlja jabuku
apple = Apple()

all_spries = pygame.sprite.Group()
all_spries.add(snake)

#dodavanje i jabuke grupi sa svim sprajtovima
all_spries.add(apple)

running = True

while running:

    time.sleep(SPEED_DELAY)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_UP:
                snake.direction = UP
            if event.key == pygame.K_DOWN:
                snake.direction = DOWN
            if event.key == pygame.K_LEFT:
                snake.direction = LEFT
            if event.key == pygame.K_RIGHT:
                snake.direction = RIGHT

    snake.update()
    #azuriranje stanja jabuke
    apple.update()

    screen.fill(BG_COLOR)

    #iscrtavanje svih sprajtova na prozoru
    all_spries.draw(screen)

    pygame.display.update()

time.sleep(2)
pygame.quit()

