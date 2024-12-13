# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:30:44 2021

@author: hw723
"""

import pygame
from pygame.locals import Rect, QUIT
import sys
import time
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption('SpaceShuttle')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

myFont = pygame.font.SysFont("arial", 30, True, False)
imgShuttle = pygame.image.load('ss.png')

clock = pygame.time.Clock()

img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

loc_a = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
vel = [4, 4]

loc = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
size_ship = 20
startTime = time.time()

a_image = pygame.image.load("girl.png")
ak = []
for i in range(5):
    a = pygame.Rect(a_image.get_rect())
    a.bottom = random.randint(0, SCREEN_WIDTH)
   
    # a = pygame.draw.circle(screen, (255, 255, 255), [4,2], 1)
    dy = (loc_a, vel)
    ak.append((a, dy))


       
while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    
    loc_a[0] = loc_a[0] + vel[0]
    loc_a[1] = loc_a[1] + vel[1]
     
    if loc_a[0] >= SCREEN_WIDTH:
        vel[0] = -vel[0]
    
    if loc_a[0] <= 0:
        vel[0] = -vel[0]
    
    if loc_a[1] >= SCREEN_HEIGHT:
        vel[1] = -vel[1]
        
    if loc_a[1] <= 0:
        vel[1] = -vel[1]
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc[0] -= 3
        
    if keys[pygame.K_RIGHT]:
        loc[0] += 3
        
    if keys[pygame.K_UP]:
        loc[1] -= 3
        
    if keys[pygame.K_DOWN]:
        loc[1] += 3
        
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            
    
    
    time_diff = str(time.time()- startTime)
    currentTime_text = myFont.render(time_diff , 1, (255, 255, 255))
    pygame.draw.circle(screen, (255, 255, 255), loc, size_ship, 1)
    
    # pygame.draw.circle(screen, (255, 255, 255), loc_a, size_ship, 1)

    for (a, dy) in ak:
        screen.blit(a_image, a)
        
    loc_TL = [loc[0] - img_width/2, loc[1] - img_height/2]
    screen.blit(imgShuttle, loc_TL)

    screen.blit(currentTime_text, [SCREEN_WIDTH-70, 20])
    
    pygame.display.update()
