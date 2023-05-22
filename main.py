import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("SpaceCat")

x = 50
y = 50
x1 = 250
y1 = 250
w = 15
h = 15
speed = 8

pygame.mixer.music.load('mus/zvuk-bushuyuschego-ognya-plamya-27572.mp3')
pygame.mixer.music.play()


ef = pygame.mixer.Sound('mus/korotkiy-zvuk-kaminnogo-spokoynogo-ognya.mp3')
ef.set_volume(0.25)


i=0
bg = pygame.image.load('img/bg.jpg')
cat = [
    pygame.image.load('img/1.png'),
    pygame.image.load('img/2.png'),
    pygame.image.load('img/3.png'),
    pygame.image.load('img/4.png'),
    pygame.image.load('img/5.png'),
]
wcat = 130
hcat = 130
cat1 = [
    pygame.transform.scale(cat[0],(wcat,hcat)),
    pygame.transform.scale(cat[1],(wcat,hcat)),
    pygame.transform.scale(cat[2],(wcat,hcat+10)),
    pygame.transform.scale(cat[3],(wcat,hcat+10)),
    pygame.transform.scale(cat[4],(wcat,hcat))
]


def drawWindow():
    global i
    if i < 4:
        i += 1
    else:
        i=0
    win.blit(bg, (0,0))
    win.blit(cat1[i], (x,y))

    pygame.draw.rect(win, (0, 200, 0), (x1, y1, w, h))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and y<500-h:             #кнопка вниз
        y += speed
        ef.play()
    if keys[pygame.K_UP] and y>0:             #кнопка вверх
        y -= speed
        ef.play()
    if keys[pygame.K_LEFT] and x>0:             #кнопка влево
        x -= speed
        ef.play()
    if keys[pygame.K_RIGHT] and x<500-w:             #кнопка вправо
        x += speed
        ef.play()

    drawWindow()



pygame.quit()



