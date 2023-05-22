import pygame
import random

pygame.init()
win = pygame.display.set_mode((1000,600))


x = 50
y = 50
h = 60
w = 60
speed = 8

x1 = 250
y1 = 250
h1 = 60
w1 = 60
speed1 = 8

d=5
col = 255

bg = pygame.image.load('img/bg.jpg')
cat = [
    pygame.image.load('img/Vector 3.png'),
    pygame.image.load('img/Vector 4.png'),
    pygame.image.load('img/Vector 5.png'),

    pygame.image.load('img/Vector 6.png'),
    pygame.image.load('img/Vector 7.png'),
]
cat1 = [
    pygame.transform.scale(cat[0], (100,100)),
    pygame.transform.scale(cat[1], (100,100)),
    pygame.transform.scale(cat[2], (100,100)),
    pygame.transform.scale(cat[3], (100,100)),
    pygame.transform.scale(cat[4], (100,100))
]
i = 0
def drawWindow():
    global i
    if i < 4:
        i = i + 1
    else:
        i = 0
    win.blit(bg, (0,0))
    win.blit(cat1[i],(x,y))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x<1000 - w:
        x += speed
    if keys[pygame.K_LEFT] and x>0:
        x -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_UP]:
        y -= speed

    drawWindow()




