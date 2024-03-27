import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))

font = pygame.font.SysFont("Consolas", 25)
running = True
text = ''
presses_key = ''

end_text = font.render(f'Prekini', True, (0,0,0))
end_text_rect = end_text.get_rect(topleft=(0,30))

screen.blit(end_text, end_text_rect)
sat = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # provera da li je klinuto misem
        if event.type == MOUSEMOTION:
            pritisnuto = pygame.mouse.get_pressed()[0]
            pos = pygame.mouse.get_pos() #uzima se pozicija na kojoj je kliknuto
            if end_text_rect.collidepoint(pos) and pritisnuto: #proverava se da li je u
                                                 #okviru pravugaonika kojim je odredjen tekst Pokreni

                running = False  #daje se signal za prekid glavne petlje

        if event.type == KEYDOWN:
            presses_key = event.unicode
            text+= presses_key

            word = font.render(text, True, pygame.Color("red"))
            screen.blit(word, (0,0))

        pygame.display.update()
        sat.tick(20)

pygame.quit()
