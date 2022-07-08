import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((0, 260))
    
    def write_score(self, points):
        self.clear()
        self.write(f"Score: {points}", False, "center", font=("Verdana", 20, "normal"))
    
    def game_over(self, points):
        self.goto((0.00, 0.00))
        self.clear()
        self.write(f"Game over. Your points: {points}", False, "center", font=("Verdana", 30, "normal"))