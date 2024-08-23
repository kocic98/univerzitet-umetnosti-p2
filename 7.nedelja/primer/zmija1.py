import pygame
import time

SPEED_DELAY = 0.1  #vreme cekanja izmadju prikaza dva uzastopna koraka
STEP_SIZE = 20 	 #velicina koraka
BG_COLOR = (0,0,0)  #boja pozadine

#velicina prozora
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# pravac kretanja
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pygame.init() #inicijalizacija modula

#pravljenje prozora za prikaz
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#naslov prozora
pygame.display.set_caption("Igra Zmijica")

#promenljiva za kontrolu petlje igre
running = True

#klasa koja predstavlja zmiju
class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_seg.gif")< #pravljenje slike glave zmije
        self.rect = self.image.get_rect() #pravljenje pridruzenog  pravugaonika
        self.direction =  DOWN  #odredjivanje pravca kretanja zmije

    #metod za azuriranje stanja zmije
    def update(self):
        #pomeranje polozaja zmije prema trenutnom pravcu kretanja
        if self.direction == UP:
            self.rect.top -= STEP_SIZE

        elif self.direction == DOWN:
            self.rect.top += STEP_SIZE

        elif self.direction == LEFT:
            self.rect.left -= STEP_SIZE

        elif self.direction == RIGHT:
            self.rect.left += STEP_SIZE

        #onemogucavanje izlaska zmije van prozora
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

#pravljenje objekta koji ce predstavljati zmiju
snake=Snake()

#pravljenje grupe koja ce sadrzati sve sprajtove
all_spries = pygame.sprite.Group()

#dodavanje zmije u grupu
all_spries.add(snake)

#petlja igre (tj. glavna petlja)
running = True

while running:

    #zamrzavanje prikaza radi boljeg pracenja svakog koraka
    time.sleep(SPEED_DELAY)

    #obrada dogadjaja
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            #odredjivanje pravca kretanja zmije na osnovu pritisnutog tastera
            if event.key == pygame.K_UP:
                snake.direction = UP
            if event.key == pygame.K_DOWN:
                snake.direction = DOWN
            if event.key == pygame.K_LEFT:
                snake.direction = LEFT
            if event.key == pygame.K_RIGHT:
                snake.direction = RIGHT

    #azuriranje stanja zmije
    snake.update()

    #postavljanje boje prozora
    screen.fill(BG_COLOR)

    #iscrtavanje svakog sprajta
    all_spries.draw(screen)

    #azurira sadrzaj za prikazivanje
    pygame.display.update()

pygame.quit()

