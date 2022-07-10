from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
    
    def spawn(self):
        x_pos = random.randrange(-280, 280, 20)
        y_pos = random.randrange(-280, 280, 20)
        self.goto(x_pos, y_pos)
        print(self.position())

    def get_position(self):
        return self.position()


