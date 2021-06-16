# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption('SpaceShuttle')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("arial", 30, True, False)
loc = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
vel = [4, 4]
ak =[]
for i in range(5):
    a = pygame.draw.circle(screen, (255, 255, 255), loc, 10)
    ak.append(a)
    
    
while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    if loc[0] >= SCREEN_WIDTH:
        vel[0] = -vel[0]
    
    if loc[0] <= 0:
        vel[0] = -vel[0]
    
    if loc[1] >= SCREEN_HEIGHT:
        vel[1] = -vel[1]
        
    if loc[1] <= 0:
        vel[1] = -vel[1]
    
    
    loc_text = myFont.render(str(loc), 1, (255, 255, 255))
    screen.blit(loc_text, [20, 20])
    loc_text = myFont.render(str(vel), 1, (255, 255, 255))
    screen.blit(loc_text, [200, 20])
    
    pygame.draw.circle(screen, (255, 255, 255), loc, 10)
    pygame.display.update()