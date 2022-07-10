from turtle import Turtle, forward
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color(random.choice(COLORS))
        self.turtle.penup()
        self.turtle.setheading(180)
        self.turtle.shape("square")
        self.turtle.shapesize(1, 2)

    def spawn(self, xpos, ypos):
        self.turtle.goto((xpos, ypos))
        
    def move(self, round):
        self.turtle.forward(5 + (round * MOVE_INCREMENT))

    def check_collision(self, turtle):
        if self.turtle.distance(turtle) < 20:
            return True
        
        
