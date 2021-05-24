# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:10:30 2021

@author: user
"""

import turtle
def outline():
    tline= turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()
    
    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
    
outline()

asteroid = turtle.Turtle()
asteroid.shape("circle")

loc = [100, 100]
vel = [4 ,-4]

asteroid.goto(loc[0], loc[1])

for i in range(600):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    if loc[0] >= SCREEN_WIDTH/2:
        loc[0] = SCREEN_WIDTH/2*2 - loc[0]
        vel[0] = -vel[0]
    
    if loc[0] <= -SCREEN_WIDTH/2:
        loc[0] = -SCREEN_WIDTH/2*2 - loc[0]
        vel[0] = -vel[0]
        
    if loc[1] >= SCREEN_HEIGHT/2:
        loc[1] = SCREEN_HEIGHT/2*2 - loc[1]
        vel[1] = -vel[1]
        
    if loc[1] <= -SCREEN_HEIGHT/2:
        loc[1] = -SCREEN_HEIGHT/2*2 - loc[1]
        vel[1] = -vel[1]
        
    asteroid.goto(loc[0], loc[1])
    
turtle.exitonclick()
turtle.bye()