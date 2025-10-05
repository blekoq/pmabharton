import time 
from turtle import *

blekoq=Turtle()
blekoq.shape("turtle")
blekoq.color("green")
blekoq.pensize(3)
blekoq.fillcolor("red")
blekoq.begin_fill()
for i in range(4):
    blekoq.forward(100)
    blekoq.right(90)
blekoq.end_fill()
blekoq.forward(50)
for i in range(20):
    blekoq.forward(10)
    blekoq.right(18)
time.sleep(10)