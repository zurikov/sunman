#
# SUNMAN
#
# By @zurikov
#
# Version: 0.1.0
#   Last update: 3rd July, 2022
#
# Come to see new updates on my GitHub!
#
    
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("SUNMAN")

walkRight = pygame.image.load('sunman_right.png')
walkLeft = pygame.image.load('sunman_left.png')
playerStand = pygame.image.load('sunman.png')

clock = pygame.time.Clock()
x = 100
y = 400
width = 80
height = 80
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount 
    win.fill((0,0,0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft, (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight, (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 5:
        x -= speed
        left = True
        right = False
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 500 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                 y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    drawWindow()
pygame.quit()
