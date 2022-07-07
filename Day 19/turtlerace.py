from traceback import print_tb
import turtle
import random

from numpy import empty

#tim = turtle.Turtle()
screen = turtle.Screen()
colors = ["red", "blue", "yellow", "green", "purple"]
startpos = 200
game_on = True
winning_turtle = None

screen.setup(500, 400)
turtles = []
for color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    
    turtles.append(new_turtle)

for turtl in turtles:    
    turtl.setposition(x=(-230, startpos))
    startpos -= 100

user_bet = screen.textinput("Bet", "Bet which turtle gonna win the race. Enter color: ")

def move(turtle):
    turtle.forward(random.randrange(0, 10))

def check_win(turtle):
    if turtle.position()[0] >= 230.00:
        return True
    else:
        return False

while game_on:
    for turt in turtles:
        move(turt)
    for turt in turtles:
        if check_win(turt):
            winning_turtle = turt
            game_on = False

if winning_turtle.color()[0] == user_bet:
    print("Congratulation you have won!")
else:
    print("You lost!")

screen.exitonclick()