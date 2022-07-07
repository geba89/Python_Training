from email.utils import parsedate_to_datetime
from logging import lastResort
from turtle import Screen, Turtle, update
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

#snake variables
snake = []
initial_pos = 0.00
last_part = None
head = None


#initial snake setup - size 3
for _ in range(3):
    new_part = Turtle(shape="square")
    new_part.penup()
    new_part.color("white")
    new_part.setpos(x=(initial_pos, 0.00))
    initial_pos -= 20.00
    snake.append(new_part)

head = snake[0]
screen.update()

def increase_snake_size(last):
    last_pos = last.xcor()
    last = new_snake_part(last_pos)
    return last

def new_snake_part(last_pos):
    new_part = Turtle(shape="square")
    new_part.penup()
    new_part.color("white")
    new_part.setpos(x=(last_pos - 20, 0.00))    
    return new_part

def follow(part_to_follow, followers):    
    prev_follower = part_to_follow
    new_position = prev_follower.position()
    part_to_follow.forward(20)   
    for follower in followers:
        if follower == head:
            continue
        prev_position = follower.position()
        follower.goto(new_position)
        new_position = prev_position

def turn_right():
    head.right(90)

def turn_left():
    head.left(90)

screen.listen()

while game_on:    
    last_part = snake[len(snake)-1]
    screen.onkey(turn_right, 'd')
    screen.onkey(turn_left, 'a')
    follow(head, snake)
    time.sleep(0.1)
    screen.update()

# last_part = increase_snake_size(last_part)
# snake.append(last_part)
# print(last_part)



screen.exitonclick()