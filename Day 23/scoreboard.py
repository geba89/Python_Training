from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.setposition((-220, 250))
        self.round = 0
        self.scoreboard.penup()
    
    def write_round(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Round {self.round}", False, "center", font=("Verdana", 15, "bold"))

    def write_game_over(self):
        self.scoreboard.setposition((0, 0))
        self.scoreboard.clear()
        self.scoreboard.write(f"Game Over. Final score: {self.round - 1}", False, "center", font=("Verdana", 25, "bold"))
