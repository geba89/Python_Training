from turtle import Turtle

class Paddle:
    def __init__(self, speed):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(5, 1, None)
        self.paddle.penup()
        self.speed = speed

    def spawn(self, pos_x, pos_y):
        self.paddle.goto((pos_x, pos_y))

    def move_up(self):
        pos_y = self.paddle.ycor()  
        pos_y += self.speed
        pos_x = self.paddle.xcor()
        self.paddle.goto(pos_x, pos_y)

    def move_down(self):
        pos_y = self.paddle.ycor()  
        pos_y -= self.speed
        pos_x = self.paddle.xcor()
        self.paddle.goto(pos_x, pos_y)




