from turtle import Turtle
import turtle
import random

timmy = Turtle()
screen = turtle.Screen()
timmy.color("coral")
screen.colormode(255)

for i in range(3, 11):
    angle = 360/i
    for j in range(i):
        timmy.forward(100)
        timmy.right(angle)
        timmy.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))



screen.exitonclick()