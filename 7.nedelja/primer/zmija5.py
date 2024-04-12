import pygame, time
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

#definisanje dogadjaja koji oznacava da je zmija ujela sebe
SELFBITE = pygame.USEREVENT + 1

font = pygame.font.SysFont("Consolas", 25)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_seg.gif")
        self.rect = self.image.get_rect()
        self.tail = []
        self.direction =  DOWN
        self.applesNum = 0

    def update(self, apple):

        self.tail.append(Point(self.rect.left, self.rect.top))

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

        if (self.rect.left == apple.rect.left) & (self.rect.top == apple.rect.top):
            apple.live = False
            self.applesNum+=1

        #provera da li je zmija ujela sebe
        elif self.snakeIsTangled():
            #ako jeste signalizira se dogadjaj SELFBITE
            pygame.event.post(pygame.event.Event(SELFBITE))
        else:
            self.tail.pop(0)

    #metod za proveru da li je zmija ujela sebe
    def snakeIsTangled(self):
        #za svaki deo u repu
        for tailSeg in self.tail:
            #proverava se da li mu je gornji levi ugao isti kao
            #gornji levi ugao glave
            if self.rect.top == tailSeg.y and snake.rect.x == tailSeg.x:
                return True
        return False

    def drawTail(self, where):
        halfStep = STEP_SIZE / 2
        for tailSeg in self.tail:
            pygame.draw.circle(where, (10, 200, 10),
                               (tailSeg.x + halfStep, tailSeg.y + halfStep), STEP_SIZE / 2, 2)


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

        #obrada dogadjaja kada zmija ujede sebe
        elif  event.type == SELFBITE:
            running = False #zavrsava se igrica

    snake.update(apple)
    apple.update()

    screen.fill(BG_COLOR)

    all_spries.draw(screen)

    snake.drawTail(screen)

    if running:
        message = f"Number of apples: {snake.applesNum}"
    else:
        message = "Bye-Bye"

    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, text.get_rect(topleft=(0, SCREEN_HEIGHT-text.get_height())))

    pygame.display.update()

time.sleep(2)
pygame.quit()

