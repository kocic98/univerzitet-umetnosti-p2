
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

#postavljanje fonta koji ce biti koriscen za prikaz teksta
font = pygame.font.SysFont("Consolas", 25)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Igra Zmijica")

running = True

class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_seg.gif")
        self.rect = self.image.get_rect()
        self.direction =  DOWN
        self.applesNum = 0 #atribut cuva podatak koliko jabuka je zmija pojela

    def update(self, apple): #metodu se prosledjuje i jabuka radi provere da li je zmija jede

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

        #provera da li zmija jede jabuku
        if (self.rect.left == apple.rect.left) and (self.rect.top == apple.rect.top):
            apple.live = False #ako je zmija pojela jabuku vise se ne prikazuje
            self.applesNum+=1  #povecava se broj pojedenih jabuka
                                #napomena: pri narednom pozivu metoda za jabuku
                                # (apple.update()) odredice se nova pozicija za jabuku
                                # na prozoru

class Apple(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.gif")
        self.rect = self.image.get_rect()
        self.live = False

    def update(self):
        if not self.live:
            self.rect.top = randint(0, SCREEN_HEIGHT - STEP_SIZE)
            self.rect.top -= self.rect.top % STEP_SIZE
            self.rect.left = randint(0, SCREEN_WIDTH - STEP_SIZE)
            self.rect.left -= self.rect.left % STEP_SIZE
            self.live = True

snake=Snake()
apple = Apple()

all_spries = pygame.sprite.Group()
all_spries.add(snake)
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

    snake.update(apple)
    apple.update()

    screen.fill(BG_COLOR)
    all_spries.draw(screen)

    #pravljenje poruke za ispis
    if running:
        message = f"Number of apples: {snake.applesNum}"
    else:
        message = "Bye-Bye"

    # pravljenje slike za poruku
    text = font.render(message, True, (255, 255, 255))
    #prikaz poruke na prozoru u donjem levom uglu
    screen.blit(text, text.get_rect(topleft=(0, SCREEN_HEIGHT-text.get_height())))

    pygame.display.update()

time.sleep(1)
pygame.quit()

