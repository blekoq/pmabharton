from turtle import *
import time
turtle=Turtle()
screen=Screen()
screen.screensize(600,600)
turtle.width(5)
turtle.pencolor("cyan")
turtle.shape("classic")
for i in range(8):
    for x in range(4):
        turtle.forward(50)
        turtle.left(75)
        turtle.forward(50)
        turtle.circle(100)
        turtle.backward(50)
        turtle.right(75)

    for x in range(4):
        
        turtle.right(75)
        turtle.forward(50)
        turtle.backward(50)
        turtle.left(75)
        turtle.backward(50)
    turtle.left(45)

time.sleep(3)
