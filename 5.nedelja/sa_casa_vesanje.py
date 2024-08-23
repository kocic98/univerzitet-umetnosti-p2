import pygame
import random

pygame.init()
velicina_prozora = (350,150)

ekran = pygame.display.set_mode(velicina_prozora)
pygame.display.set_caption('Igra Vesanja')


def sifruj(rec="umetnost"):#funkcija koja prihvata rec i postavlja * umesto svakog slova
    sifrovana = ""
    for slovo in rec:
        sifrovana += "*"
    return sifrovana

reci = ["umetnost","programiranje","crvena","matematika"]
rec = random.choice(reci) #nasumicno se bira jedna rec iz liste reci
sifrovana = sifruj(rec)

def uneto_slovo(slovo): 
    tmp = sifrovana
    for i in range(len(rec)):
        if rec[i] == slovo:
            tmp = tmp[:i] + slovo + tmp[i+1:]
    return tmp

font = pygame.font.SysFont("Times New Roman", 40)

ekran.fill("lightblue")

ispis = font.render(sifrovana,False,"blue")
ekran.blit(ispis, (0,0))
pygame.display.update()

def crtaj_cikicu():
    if greske <= 5:
        pygame.draw.circle(ekran,"black",(300,40),20,3)
    if greske <= 4:
        pygame.draw.line(ekran,"black",(300,60),(300,90),3)
    if greske <= 3:
        pygame.draw.line(ekran,"black",(300,75),(276,55),4)
    if greske <= 2:
        pygame.draw.line(ekran,"black",(300,75),(324,55),4)
    if greske <= 1:
        pygame.draw.line(ekran,"black",(300,90),(276,110),4)
    if greske <= 0:
        pygame.draw.line(ekran,"black",(300,90),(324,110),4)


def popuni_tekst():
    ekran.blit(font.render(uneta_slova,True,"red"),(0,50))
    if greske != 0:
        preostalo = "preostalo:" + str(greske)
        ekran.blit(font.render(preostalo,True,"black"),(0,80))
    ispis = font.render(sifrovana,False,"blue")
    ekran.blit(ispis, (0,0))

running = True
greske = 6
uneta_slova = "uneta slova:"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if rec.find(event.unicode) != -1:
                sifrovana = uneto_slovo(event.unicode)
                if sifrovana == rec:
                    uneta_slova = "Bravo!"
                    pygame.event.set_blocked(pygame.KEYDOWN)
            else:
                uneta_slova += ' ' + event.unicode
                greske -= 1
                if greske == 0:
                    uneta_slova = 'Cikica je mrtav.'
                    pygame.event.set_blocked(pygame.KEYDOWN)
    ekran.fill("lightblue")
    crtaj_cikicu()
    popuni_tekst()
    pygame.display.update()


pygame.quit()
