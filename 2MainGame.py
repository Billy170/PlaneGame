import random
import pygame
import time

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

lives = 4

escbtn = 0

startgame = 0

import pygame

pygame.init()

font = pygame.font.Font(None, 36)
text = font.render('Hello, Pygame!', True, (255, 255, 255))


bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

clicked = False
counter = 0

Start=time.time()

from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT

)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('en1.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.surf = pygame.Surface((35, 15))
        self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load('en2.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(5,10)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right <0:
            self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.surf = pygame.Surface((35, 15))
        self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load('en3.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(15,25)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right <0:
            self.kill()

class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy3, self).__init__()
        self.surf = pygame.Surface((35, 15))
        self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load('planet1.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(6,10)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right <0:
            self.kill()

class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy4, self).__init__()
        self.surf = pygame.Surface((35, 15))
        self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load('planet2.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(4,8)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right <0:
            self.kill()

class button():
    # colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

start: button = button(800, 400, 'start')
quit = button(1050, 400, 'Quit')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()


enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


ADDENEMY1 = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY1, 2000)
ADDENEMY2 = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY2, 5000)
ADDENEMY3 = pygame.USEREVENT + 3
pygame.time.set_timer(ADDENEMY3, 50000)
ADDENEMY4 = pygame.USEREVENT + 4
pygame.time.set_timer(ADDENEMY4, 500000)


bg = pygame.image.load("bg.PNG")
hp0 = pygame.image.load("hp0.PNG")
hp1 = pygame.image.load("hp1.PNG")
hp2 = pygame.image.load("hp2.PNG")
hp3 = pygame.image.load("hp3.PNG")
hp4 = pygame.image.load("hp4.PNG")


Font1 = pygame.font.SysFont("comicsansms", 50, True, True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                escbtn = 1
                startgame = 0
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY1 and startgame == 1:
            new_enemy1 = Enemy1()
            new_enemy2 = Enemy2()
            new_enemy3 = Enemy3()
            new_enemy4 = Enemy4()
            enemies.add(new_enemy1)
            all_sprites.add(new_enemy1)
            enemies.add(new_enemy2)
            all_sprites.add(new_enemy2)
            enemies.add(new_enemy3)
            all_sprites.add(new_enemy3)
            enemies.add(new_enemy4)
            all_sprites.add(new_enemy4)

    screen.blit(bg, (0, 0))
    if escbtn == 1:
        if start.draw_button():
            print('start')
            startgame = 1
            escbtn = 0
        if quit.draw_button():
            print('Quit')
            running = False
    if startgame == 1:
        if pygame.sprite.spritecollideany(player, enemies):
            en = pygame.sprite.spritecollideany(player, enemies)
            en.kill()
            lives = lives - 1
        if lives == 4:
            screen.blit(hp4, (0, 0))
        elif lives == 3:
            screen.blit(hp3, (0, 0))
        elif lives == 2:
            screen.blit(hp2, (0, 0))
        elif lives == 1:
            screen.blit(hp1, (0, 0))
        elif lives == 0:
            screen.blit(hp0, (0, 0))
        elif lives <= 0:
            exit()
    if startgame == 1:
        TrexonOra = time.time()
        Time1 = Font1.render(str(round(TrexonOra-Start,2)), True, (255, 255, 255))
        screen.blit(Time1, (300, 35))
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)


    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(160)