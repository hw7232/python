# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:19:43 2021

@author: papple
"""

import turtle
import random

while True:
    victory = turtle.textinput("경주게임","빨강 or 파랑")
    if victory == "빨강" or victory == "파랑":
        break

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.up()
t1.goto(0,200)
t1.down() 

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.up()
t2.goto(0,-200)
t2.down()

t3 = turtle.Turtle()

font_a = ("굴림", 15)
font_b = ("굴림", 15)

while True:
    t1_move = random.randrange(0, 10)
    t2_move = random.randrange(0, 10)

    t1_x = t1.xcor()
    t2_x = t2.xcor()

    t1.setx(t1_x + t1_move)
    t2.setx(t2_x + t2_move)


    if t1_x >= 300 or t2_x >= 300:
        if t1_x > t2_x:
            t1.write("승리", font = font_b)
            if victory == "파랑":
                t3.write("맞췄습니다.", font = font_a)
            else:
                t3.write("틀렸습니다.", font = font_a)
            break
        elif t1_x < t2_x:
           t2.write("승리",font = font_b)
           if victory == "파랑":
               t3.write("틀렸습니다.", font = font_a)
           elif victory == "빨강":
               t3.write("맞췄습니다.", font = font_a)
           break
        elif t1_x == t2_x:
            t1.write("승리", font = font_b)
            if victory == "파랑":
                t3.write("맞췄습니다.")
            else:
                t3.write("틀렸습니다.")
            break  
        
    
    print("t1:", t1_x, "vs t2:", t2_x)
print("끝")


turtle.mainloop()