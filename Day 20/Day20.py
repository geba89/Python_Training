from turtle import Screen
import time
from snake import Snake

#variables
game_on = True

#initialize screen and set it up
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#create snake and refresh screen
my_snake = Snake()
screen.update()

#controls
screen.listen()
screen.onkey(my_snake.turn_right, 'd')
screen.onkey(my_snake.turn_left, 'a')
screen.onkey(my_snake.increase_snake_size, 'c')

#game loop
while game_on:    
    my_snake.set_last_part()    
    my_snake.follow()
    time.sleep(0.1)
    screen.update()


#exit
screen.exitonclick()