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

spaceShip = turtle.Turtle()
spaceShip.shape("turtle")
screen = spaceShip.getscreen()
ship_loc = [0, 0]
def moveLeft( ):
    ship_loc[0] = ship_loc[0] - 1

def moveRight( ):
    ship_loc[0] = ship_loc[0] + 1
    
def moveUp( ):
    ship_loc[1] = ship_loc[1] + 1

def moveDown( ):
    ship_loc[1] = ship_loc[1] - 1
    
    
    
screen.onkeypress(moveLeft, "Left")
screen.onkeypress(moveRight, "Right")
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")

screen.listen( )

for i in range(600):
    spaceShip.goto(ship_loc[0], ship_loc[1])
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