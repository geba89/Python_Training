import turtle

from sympy import content

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((0, 260))
        self.highscore = 0
        self.highscore = self.get_highscore()
        
    
    def write_score(self, points):
        self.clear()
        self.set_highscore(points)
        self.write(f"Score: {points} / High Score: {self.highscore}", False, "center", font=("Verdana", 20, "normal"))
        
    
    def game_over(self, points):
        self.goto((0.00, 0.00))
        self.clear()
        self.write(f"Your points: {points}, thank you for playing!", False, "center", font=("Verdana", 15, "normal"))

    def set_highscore(self, score):
        if score > self.highscore:
            self.highscore = score

    def get_highscore(self):
        file = open('Day 20 and 21/score.txt')
        score_read = file.read()
        file.close()
        return int(score_read)

    def write_highscore(self):
        file = open('Day 20 and 21/score.txt', "w")       
        file.write(str(self.highscore))
        file.close()