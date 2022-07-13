from queue import Empty
import pandas as p
import turtle as t
import writer
import states

screen = t.Screen()
image = 'Day 25/Map Game/blank_states_img.gif'
screen.addshape(image)
t.shape(image)
game_on = True
points = 0
max_points = 50

name_writer = writer.Writer()
state_guesser = states.States('Day 25/Map Game/50_states.csv')

while game_on:
    state_guess = screen.textinput("State Quesser", "Please enter state name: ")    
    guess = state_guesser.get_cords(state_guess)
    if guess.empty:
        game_on = False
        name_writer.game_over(points)
    else:
        points += 1
        print(guess)
        name_writer.write_state_name(guess['x'], guess['y'], state_guess)
    if points == max_points:
        game_on = False
        
screen.exitonclick()