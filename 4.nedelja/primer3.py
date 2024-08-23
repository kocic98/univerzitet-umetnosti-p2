import pygame  #ucitavanje biblioteke
from pygame.locals import *

pygame.init()  #inicijalizacija modula

"""
            550
--------------------------------------
| pogodjeno -> pos (20, 10)          |
| uneto    -> pos (20, 50)           |     200
| broj pokusaja -> pos (20, 90)      |
| poruka  -> pos (20, 130)           |
| zavrsetak igre -> pos (20, 170)    |
--------------------------------------
"""

#postavljanje boja
BLACK = (0, 0, 0)
PURPLE = (205, 0, 205)
YELLOW = (255, 255, 155)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
background = YELLOW

#velicina prozora
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 200

#funkcija vraca sve indekse karaktera char u string
def all_indices(string, char):
    indices = []
    for ind, c in enumerate(string):
        if c==char:
            indices.append(ind)
    return indices

#pravljenje prozora
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Igrica Vešanje")  #postavljanje naslova
screen.fill(background)  #postavljanje pozadine

guess = 'umetnost'  #rec za pogadjanje
text = '*'*len(guess)  #niska sadrzi * onoliko puta kolika je duzina reci za pogadjanje

#postavljanje fonta koji ce biti koriscen za prikaz teksta
font = pygame.font.SysFont("Consolas", 25)

#definisanje pozicija gornjeg levog ugla razlicitih tekstova koji ce biti prikazani
word_pos = (20, 10)
character_pos = (20, 50)
attempts_pos = (20, 90)
mess_pos = (20, 130)
end_pos = (20, 170)

running = True  #promenljiva za glavnu petlju

pressed_key = ''  #promenljiva za karakter pritisnutog tastera
attempts = 0      #broj promasaja

#pravljenje slika za tekstove
word = font.render(text, True, PURPLE)
character = font.render(f'Uneto: {pressed_key}', True, BLUE)
num_attempts = font.render(f'Broj promašaja: {attempts}', True, BLUE)
end_text = font.render(f'Prekini', True, BLACK)
end_text_rect = end_text.get_rect(topleft=end_pos)   #vraca se Rect koji je pridruzen tekstu Prekini

#dodavanje tekstova na prozor
screen.blit(word, word_pos)
screen.blit(character, character_pos)
screen.blit(num_attempts, attempts_pos)
screen.blit(end_text, end_text_rect)

#petlja igre, tj. glavna petlja
while running:

    #obrada dogadjaja
    for event in pygame.event.get():
        if event.type == QUIT:   #provera da li je kliknuto na dugme za zatvaranje prozora
            running = False

        if event.type == MOUSEBUTTONUP: # provera da li je klinuto misem
            pos = pygame.mouse.get_pos()  #uzima se pozicija na kojoj je kliknuto
            if end_text_rect.collidepoint(pos):  #proverava se da li je u
                                                 #okviru pravugaonika kojim je odredjen tekst Pokreni
                running = False

        if event.type == KEYDOWN:  #provera da li je pritisnut taster
            pressed_key = event.unicode   #uzima se pridruzeni karakter
            screen.fill(background)  #ciscenje pozadine da ne bi bilo preklapanja starog i novog teksta

            #indeksi zadatog karaktera
            indices = all_indices(guess, pressed_key)

            #ako se zadati karakter ne nalazi u reci za pogadjanje
            # povecava se broj neuspelih pogadjanja
            if len(indices)==0:
                attempts+=1
            else:
                for ind in indices:
                    text= f'{text[:ind]}{pressed_key}{text[ind+1:]}'

            #novi prikaz tekstova
            word = font.render(text, True, PURPLE)
            character = font.render(f'Uneto: {pressed_key}', True, BLUE)
            num_attempts = font.render(f'Broj promašaja: {attempts}', True, BLUE)

            screen.blit(word, word_pos)
            screen.blit(character, character_pos)
            screen.blit(num_attempts, attempts_pos)
            screen.blit(end_text, end_text_rect)

            if guess==text:
                screen.blit(font.render('Čestitamo!', True, BLUE), mess_pos)
                pygame.event.set_blocked(KEYDOWN)

        #azuriranje prozora
        pygame.display.update()

pygame.quit()
