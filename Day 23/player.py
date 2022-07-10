from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.shape("turtle")
        
    def spawn(self):
        self.turtle.setpos(STARTING_POSITION)

    def move(self):
        self.turtle.goto(0, self.turtle.ycor() + MOVE_DISTANCE)

    def check_finish_line(self):
        if self.turtle.ycor() >= FINISH_LINE_Y:
            return True

