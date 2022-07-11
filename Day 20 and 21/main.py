from asyncore import write
from turtle import Screen
import time
import food
from snake import Snake
import scoreboard

#variables
game_on = True
points = 0
score = scoreboard.Scoreboard()
pause = False

def set_pause():
    global pause
    pause = not pause

def quit_game():
    global game_on
    game_on = False

#initialize screen and set it up
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
score.write_score(points)


#create snake and refresh screen
my_snake = Snake()
screen.update()

print((100.00, 200.00) == (100.00, 200.00))
#controls
screen.listen()
screen.onkey(my_snake.turn_right, 'd')
screen.onkey(my_snake.turn_left, 'a')
screen.onkey(my_snake.increase_snake_size, 'c')
screen.onkey(set_pause, 'p')
screen.onkey(quit_game, 'q')

food1 = food.Food()
food1.spawn()

#game loopaaa
while game_on:      
    if food1.distance(my_snake.head) <= 5:
        my_snake.increase_snake_size()
        food1.spawn()
        points += 1
        score.write_score(points)
    my_snake.set_last_part()   
    my_snake.follow(pause)    
    time.sleep(0.1)
    screen.update()

    #check if outside of map and go to other part of map:
    if my_snake.head.position()[0] > 300.00:
        my_snake.head.goto(-300.00, (my_snake.head.position()[1])) 
    elif my_snake.head.position()[0] < -300.00:
        my_snake.head.goto(300.00, (my_snake.head.position()[1])) 
    elif my_snake.head.position()[1] > 300.00:
        my_snake.head.goto((my_snake.head.position()[0], -300))
    elif my_snake.head.position()[1] < -300.00:
        my_snake.head.goto((my_snake.head.position()[0], 300)) 

    #check collision with tail:
    collided = my_snake.check_collision_with_tail()
    if collided:
        my_snake.reset_snake()
        points = 0
        score.write_score(points)
        score.write_highscore()
    
score.game_over(points)
score.write_highscore()

#exit
screen.exitonclick()