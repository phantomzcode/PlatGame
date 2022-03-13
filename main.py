#importing
import pygame
import sys
from pygame.locals import *
import random

#init window and fps
w_size = (800, 600)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(w_size)
pygame.display.set_caption('PlatGame(60 FPS(framerate/framepersecond))')

#images
playerblueimg = pygame.image.load('img/playerblue.png')
playergreenimg = pygame.image.load('img/playergreen.png')
playerredimg = pygame.image.load('img/playerred.png')
coin10expimg = pygame.image.load('img/coin10exp.png')

#position variables
movingleft = False
movingright = False
movingup = False
movingdown = False
playerposition = [800 / 2 - 16, 600 / 2 - 16]
coin10exppos = [random.randint(100, 700), random.randint(100, 500)]

#collision rectangles
playerrect = pygame.Rect(playerposition[0], playerposition[1], playerblueimg.get_width(), playerblueimg.get_height())
coin10exprect = pygame.Rect(coin10exppos[0], coin10exppos[1], coin10expimg.get_width(), coin10expimg.get_height())

#other variables

#game update and loop
while True:
    screen.fill((50, 168, 82))
    screen.blit(playerblueimg, playerposition)
    screen.blit(coin10expimg, coin10exppos)
    if movingleft == True:
        playerposition[0] -= 1
    if movingright == True:
        playerposition[0] += 1
    if movingup == True:
        playerposition[1] -= 1
    if movingdown == True:
        playerposition[1] += 1

    playerrect.x = playerposition[0]
    playerrect.y = playerposition[1]
    coin10exprect.x = coin10exppos[0]
    coin10exprect.y = coin10exppos[1]

    if playerrect.colliderect(coin10exprect):
        coin10exprect.x = coin10exppos[0]
        coin10exprect.y = coin10exppos[1]
        coin10exppos = [random.randint(100, 700), random.randint(100, 500)]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                movingright = True
            if event.key == K_LEFT:
                movingleft = True
            if event.key == K_UP:
                movingup = True
            if event.key == K_DOWN:
                movingdown = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                movingright = False
            if event.key == K_LEFT:
                movingleft = False
            if event.key == K_UP:
                movingup = False
            if event.key == K_DOWN:
                movingdown = False

    pygame.display.update()
    clock.tick(160)
