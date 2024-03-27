import pygame   #ucitavanje biblioteke pygame
from pygame.locals import *
from math import pi

pygame.init()  #inicijalizacija modula

"""
            550
--------------------------------------------------------
| pogodjeno -> pos (20, 10)          |                 |
| uneto    -> pos (20, 50)           |   povrsina      |   200
| broj pokusaja -> pos (20, 90)      |  (surface)      |
| poruka  -> pos (20, 130)           |   za crtanje    |
| zavrsetak igre -> pos (20, 170)    |   cikice        |
--------------------------------------------------------

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

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 200


def all_indices(string, char):
    indices = []
    for ind, c in enumerate(string):
        if c==char:
            indices.append(ind)
    return indices

def add_extremity(angle, width):
    arm=pygame.Surface((50,width))
    arm.set_colorkey(YELLOW)
    arm.fill(BLUE)
    newarm = pygame.transform.rotate(arm, angle)
    rect = newarm.get_rect()

    return (newarm, rect)

#funkcija za crtanje cikice u povrsini surface
#delovi se crtaju zavisno od broja promasaja (attempt)
def add_body_part(surface, attempt):

    #crtanje glave
    if attempt >= 1:
        pygame.draw.circle(surface, BLUE, (100, 60), 30, 2)

    #crtanje jednog oka
    if attempt >= 2:
        pygame.draw.circle(surface, GREEN, (90, 50), 5)

    #crtanje drugog oka
    if attempt >= 3:
        pygame.draw.circle(surface, GREEN, (110, 50), 5)

    #crtanje nosa
    if attempt >= 4:
        pygame.draw.circle(surface, BLUE, (100, 60), 5)

    #crtanje usana
    if attempt >= 5:
        pygame.draw.arc(surface, PURPLE, [85, 50, 30, 30], pi, 2 * pi, 3)

    #crtanje tela
    if attempt >= 6:
        pygame.draw.rect(surface, BLUE, [95, 90, 10, 60])

    #crtanje jedne ruke
    if attempt >= 7:
        newarm, rect = add_extremity(30, 5)
        rect.bottomright = (100, 125)
        surface.blit(newarm, rect)

    #crtanje druge ruke
    if attempt >= 8:
        newarm, rect = add_extremity(-30, 5)
        rect.bottomleft = (100, 125)
        surface.blit(newarm, rect)

    #crtanje noge
    if attempt >= 9:
        newleg, rect = add_extremity(30, 8)
        rect.bottomright = (100, 175)
        surface.blit(newleg, rect)

    #crtanje druge noge
    if attempt >= 10:
        newleg, rect = add_extremity(-30, 8)
        rect.bottomleft = (100, 175)
        surface.blit(newleg, rect)


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

running = True

#pravljenje povrsine za crtanje cikice
surf = pygame.Surface((200,SCREEN_HEIGHT))
surf.fill(YELLOW)

presses_key = ''  #promenljiva za karakter pritisnutog tastera
attempts = 0      #broj pogadjanja

#pravljenje slika za tekstove
word = font.render(text, True, PURPLE)
character = font.render(f'Uneto: {presses_key}', True, BLUE)
num_attempts = font.render(f'Broj promašaja: {attempts}', True, BLUE)
end_text = font.render(f'Prekini', True, BLACK)
end_text_rect = end_text.get_rect(topleft=end_pos)

#dodavanje tekstova na prozor
screen.blit(word, word_pos)
screen.blit(character, character_pos)
screen.blit(num_attempts, attempts_pos)
screen.blit(end_text, end_text_rect)

#petlja igre
while running:

    #obrada dogadjaja
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if end_text_rect.collidepoint(pos):
                running = False

        if event.type == KEYDOWN:
            presses_key = event.unicode
            screen.fill(background)

            indices = all_indices(guess, presses_key)

            if len(indices)==0:
                attempts+=1

                #poziva se funkcija za crtanje cikice
                add_body_part(surf, attempts)

            for ind in indices:
                text= f'{text[:ind]}{presses_key}{text[ind+1:]}'

            word = font.render(text, True, PURPLE)
            character = font.render(f'Uneto: {presses_key}', True, BLUE)
            num_attempts = font.render(f'Broj promašaja: {attempts}', True, BLUE)

            screen.blit(word, word_pos)
            screen.blit(character, character_pos)
            screen.blit(num_attempts, attempts_pos)
            screen.blit(end_text, (end_text_rect))
            screen.blit(surf, (SCREEN_WIDTH-200,0))

            if attempts>=10:
                screen.blit(font.render('Izgubili ste!', True, BLUE), mess_pos)
                pygame.event.set_blocked(KEYDOWN)
            elif guess==text:
                screen.blit(font.render('Čestitamo!', True, BLUE), mess_pos)
                pygame.event.set_blocked(KEYDOWN)

        pygame.display.update()

pygame.quit()
