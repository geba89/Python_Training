from turtle import Screen
import time
import food
from snake import Snake

#variables
game_on = True
points = 0

#initialize screen and set it up
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#create snake and refresh screen
my_snake = Snake()
screen.update()

print((100.00, 200.00) == (100.00, 200.00))
#controls
screen.listen()
screen.onkey(my_snake.turn_right, 'd')
screen.onkey(my_snake.turn_left, 'a')
screen.onkey(my_snake.increase_snake_size, 'c')

food1 = food.Food()
food1.spawn()

#game loopaaa
while game_on:  
    if food1.distance(my_snake.head) <= 5:
        my_snake.increase_snake_size()
        food1.spawn()
        points += 1
    my_snake.set_last_part()   
    my_snake.follow()    
    time.sleep(0.1)
    screen.update()

#exit
screen.exitonclick()