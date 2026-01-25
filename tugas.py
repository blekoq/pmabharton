from turtle import *
import time
from random import random
turtle=Turtle()
screen=Screen()
screen.screensize(600,600)
turtle.width(5)
turtle.speed(0)
turtle.pencolor("cyan")

turtle.shape("classic")
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90) 
for i in range(8):
    for x in range(4):
        turtle.forward(50)
        turtle.left(75)
        turtle.forward(50)
        r=random()
        g=random()
        b=random()
        turtle.fillcolor(r,g,b)
        turtle.begin_fill()
        square(50)
        turtle.end_fill()
        turtle.backward(50)
        turtle.right(75)

    for x in range(4):
        
        turtle.right(75)
        turtle.forward(50)
        turtle.right(90)
        r=random()
        g=random()
        b=random()
        turtle.fillcolor(r,g,b)
        turtle.begin_fill()
        square(50)
        turtle.end_fill()
        turtle.left(90)
        turtle.backward(50)
        
        turtle.left(75)
       
        turtle.backward(50)
    turtle.left(45)

time.sleep(3)

