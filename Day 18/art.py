import turtle
import random
import colorgram
import os

from requests import head

#variables
timmy = turtle.Turtle()
screen = turtle.Screen()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, '20_001.jpg')
colors = colorgram.extract(filename, 10)
heading = "east"
painting_size = 10
dot_size = 30
space_size = dot_size * 1.5
#setting up screen
screen.colormode(255)
screen.screensize(300, 300)

#setting up timmy
timmy.speed("fastest")
timmy.penup()

#main loop
timmy.setheading(180)
timmy.forward(painting_size * space_size/2)
timmy.setheading(90)
timmy.forward(painting_size * space_size/2)
timmy.setheading(0)
for i in range(painting_size):
    for j in range(painting_size):
        timmy.forward(space_size)
        current_color = random.choice(colors)
        timmy.dot(dot_size, current_color.rgb)   
    timmy.forward(space_size)     
    timmy.setheading(270)
    timmy.forward(space_size)
    if heading == "west":
        timmy.setheading(0)
        heading = "east"
    else:
        timmy.setheading(180)
        heading = "west"

#finish it
screen.exitonclick()