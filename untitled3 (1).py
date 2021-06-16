# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:04:24 2021

@author: user
"""

import turtle

aList = []

for i in range(4):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)
    
for i in range(4):
    aList[i].right(i * 90)
  
    for j in range(4):
        
        aList[i].left(90)
        aList[i].fd(50 * i+50)
        
turtle.done()