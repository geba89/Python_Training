import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []

score = Scoreboard()
score.write_round()
player_one = Player()
player_one.spawn()

def car_spawner(num):
    for _ in range(num):
        new_car = CarManager()
        new_car.spawn(random.randrange(300, 10000, 500), random.randrange(-240, 240, 80))
        cars.append(new_car)        


screen.listen()
screen.onkey(player_one.move, 'w')


game_is_on = True
while game_is_on:   
    car_spawner(1)
    for car in cars:
        car.move(score.round) 
    time.sleep(0.1)
    for car in cars:
        if car.check_collision(player_one.turtle):
            game_is_on = False
            score.write_game_over()
    screen.update()
    finished = player_one.check_finish_line()
    if finished:
        print("Reached checkpoint")
        player_one.spawn()
        score.round += 1
        score.write_round()    

screen.exitonclick()  
    
