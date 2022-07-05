import turtle
import random

def draw_circle(size):
    loop = 360/size
    for i in range(size):
        timmy.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        timmy.circle(100)
        timmy.left(loop)
        #timmy.forward(10)

#variables
timmy = turtle.Turtle()
screen = turtle.Screen()
directions = [0, 90, 180, 270]

#setting up screen
screen.colormode(255)
screen.screensize(300, 300)

#setting up timmy
timmy.pensize(2)
timmy.speed(0)

#main loop
draw_circle(50)

#finish it
screen.exitonclick()