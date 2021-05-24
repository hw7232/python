# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:47:05 2021

@author: user
"""
import turtle

pos_list = [[100, 100],
            [100, -100],
            [-100, 100],
            [-100, -100]]
vel_list = [[2,2],
            [2, -2],
            [-2, 2],
            [-2, -2]]

t_list = []
for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_list[i][0], pos_list[i][1])
    t_list.append(t)
    
for i in range(100):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0]
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]
        
        t_list[i].goto(pos_list[i][0], pos_list[i][1])
    
turtle.exitonclick()
turtle.bye()