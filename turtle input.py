import time 
from turtle import *
blekoq=Turtle()
blekoq.speed(3)
looping=int(input("berapakali mau menggambar: "))
for i in range(looping):
    blekoq.forward(400/looping)
    blekoq.right(360/looping)
time.sleep(10)