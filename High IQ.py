import pygame, sys
from High_IQ2 import Player
pygame.init()
screen_width = 1300
screen_height = 900
pygame.display.set_caption("Platform Game")
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((800, 600))
Yours = Player(200, 200, 0, 0, 2, True)
ground = pygame.Rect(0, 570, 800, 30)
color = (255, 0, 0)
color2 = (0,120,0)
falling = False
count = 0

def jump(y, jumpcount):
    if jumpcount >= 0:
        y -= (jumpcount ** 2) * -0.5
        jumpcount -= 1

def fall(y, jumpcount):
        y -= jumpcount
        fall(y, jumpcount + 1)


while True:
    pygame.time.delay(15)
    screen.fill((155, 155, 155))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump(Yours.Y, 10)
            if event.key == pygame.K_w:
                Yours.speedy -= 15
                print("w")
            if event.key == pygame.K_s:
                Yours.speedy += 15
            if event.key == pygame.K_a:
                Yours.speedx -= 15
            if event.key == pygame.K_d:
                Yours.speedx += 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Yours.speedy += 15
            if event.key == pygame.K_s:
                Yours.speedy -= 15
            if event.key == pygame.K_a:
                Yours.speedx += 15
            if event.key == pygame.K_d:
                Yours.speedx -= 15
    yours_drawn = pygame.Rect(Yours.X, Yours.Y, 50, 50)
    Yours.X += Yours.speedx
    Yours.Y += Yours.speedy
    pygame.draw.rect(screen, color, yours_drawn)
    pygame.draw.rect(screen, color2, ground)

    if not yours_drawn.colliderect(ground):
        falling = True
    else:
        falling = False
    if falling:
        Yours.Y += count
        count += 1
    else:
        Yours.Y -= count
        count = 0
    pygame.display.update()
