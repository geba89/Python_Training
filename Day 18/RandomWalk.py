import turtle
import random

#variables
timmy = turtle.Turtle()
screen = turtle.Screen()
directions = [0, 90, 180, 270]
#setting up screen
screen.colormode(255)
screen.screensize(300, 300)
#setting up timmy
timmy.pensize(6)
timmy.speed = 0

#main loop
for i in range(200):
    timmy.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    timmy.forward(10)
    timmy.setheading(random.choice(directions))

#finish it
screen.exitonclick()