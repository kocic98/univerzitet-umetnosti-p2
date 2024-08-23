import pygame  #ucitavanje biblioteke
from pygame.locals import *

pygame.init()  #inicijalizacija modula

#sirina i visina prozora
SCREEN_WIDTH = 250
SCREEN_HEIGHT = 60

#pravljenje prozora
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#postavljanje boje pozadine
screen.fill((255,255,255))

#postavljanje fonta koji ce biti koriscen za prikaz teksta
font = pygame.font.SysFont("Consolas", 25)

#promenljiva za glavnu petlju
running = True

#promenljiva koja ce sadrzati uneti tekst
text = ''

#promenljiva koja ce sadrzati uneti karakter
presses_key = ''

#glavna petlja, tj. petlja igrice
while running:

    #obrada dogadjaja
    for event in pygame.event.get():
        if event.type == QUIT:   #provera da li je kliknuto na dugme za zatvaranje prozora
            running = False  #daje se signal za prekid glavne petlje

        if event.type == KEYDOWN:  #provera da li je pritisnut taster
            presses_key = event.unicode   #uzima se pridruzeni karakter
            text+= presses_key  #dodaje se karakter vec unetom tekstu
            screen.fill("lightblue")
            # pravljenje slike za tekst
            word = font.render(text[-15 : ], True, pygame.Color("red"))

            # dodavanje teksta na prozor
            screen.blit(word, (0,0))

        pygame.display.update()

pygame.quit()
