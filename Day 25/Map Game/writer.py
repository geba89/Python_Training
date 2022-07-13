from turtle import Turtle

class Writer:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()

    def write_state_name(self, xcor, ycor, state):
        self.turtle.goto((xcor, ycor))
        self.turtle.write(f"{state}", False, "center", font=("Verdana", 12, "normal"))
    
    def game_over(self, points):
        self.turtle.goto((0, 0))
        self.turtle.write(f"Game Over. Your correct guesses: {points}", False, "center", font=("Verdana", 17, "normal"))
    
    def game_win(self):
        self.turtle.goto((0, 0))
        self.turtle.write(f"Congratulations! You won! All states correct.", False, "center", font=("Verdana", 17, "normal"))