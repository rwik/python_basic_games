#!/usr/bin/env python3
import pygame, sys

x=50
y=50
height=20
width=20
windowSurface = pygame.display.set_mode((500, 400), 0, 32)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(windowSurface,(255,0,0),(x,y,width,height))
    pygame.display.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>1:
        x-= 1
    if keys[pygame.K_RIGHT] and x<(500-width-1):
        x+= 1
    if keys[pygame.K_UP] and y> 1:
        y-= 1    
    if keys[pygame.K_DOWN] and y <(400-height-1):
        y+= 1
    windowSurface.fill((0,0,0))



pygame.display.quit()
pygame.quit()
exit()