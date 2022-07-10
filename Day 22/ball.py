from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.speed = 3
        self.x_move = 1
        self.y_move = 1

    def move(self):        
        current_x = 0
        current_y = 0
        current_x = self.ball.xcor()
        current_y = self.ball.ycor()
        self.ball.goto((current_x + self.x_move * self.speed, current_y + self.y_move * self.speed))
    
    def bounce_of_walls(self):
        if self.ball.ycor() >= 300 or self.ball.ycor() <= -300:
            self.y_move = self.y_move * -1        

    def bounce_of_paddle(self, paddle):
        if self.ball.distance(paddle) < 40 and abs(self.ball.xcor()) > 340:           
            self.x_move = self.x_move * -1        