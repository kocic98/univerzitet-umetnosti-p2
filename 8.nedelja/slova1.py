import pygame
from pygame.locals import  K_UP,K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
import random

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_COLOR = (255,255,255)
MESS_COLOR = (0, 255, 0)

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

all_letters = pygame.sprite.Group()

for l in  "umetnost":
    letter = Letter(l)
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

        elif event.type == MOUSEBUTTONDOWN:
            point = pygame.mouse.get_pos()

            for letter in all_letters:
                if letter.rect.collidepoint(point):
                    letter.kill()
                    num+=1


    #novo iscrtavanje
    screen.fill((255, 255,255))
    all_letters.draw(screen)

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
