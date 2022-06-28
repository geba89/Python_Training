#Higher lower game

#imports
import GameData
import random
import replit
import time

def game():
    #old_to_compare = []
    #new_to_compare = {}
    game_on = True
    player_answer = ""
    correct_answer = ""
    new_to_compare = get_next()
    play_again = ""
    guesses = 0
    print("Let's start!")
    time.sleep(0.5)
    while game_on:
        old_to_compare = new_to_compare
        new_to_compare = get_next()
        while compare(old_to_compare, new_to_compare):
            new_to_compare = get_next()

        print("Who has more followers!")
        time.sleep(1)
        print(f"A : {old_to_compare['name']} who is {old_to_compare['description']} from {old_to_compare['country']}")
        time.sleep(0.5)
        print("OR")
        time.sleep(0.5)
        print(f"B : {new_to_compare['name']} who is {new_to_compare['description']} from {new_to_compare['country']}")
        time.sleep(0.2)
        print("Make your guess!")
        player_answer = input("A or B? ")

        if int(old_to_compare['follower_count']) > int(new_to_compare['follower_count']):
            correct_answer = "a"
        else:
            correct_answer = "b"
        
        if correct_answer != player_answer.lower():
            print(f"Sorry, you lost! {old_to_compare['name']} has {old_to_compare['follower_count']} and {new_to_compare['name']} has {new_to_compare['follower_count']}")
            time.sleep(0.5)
            print(f"Thanks for playing! You had correct {guesses}")
            time.sleep(0.5)
            play_again = input("Do you want to play again? y / n: ")
            if play_again == "y":
                replit.clear()
                game()
            break
            
        print("Correct! Lets go next one!")
        time.sleep(1)
        replit.clear()
        guesses += 1


def get_next():
    return random.choice(GameData.data)


def compare(old_choice, new_choice):
    if old_choice['name'] == new_choice['name']:
        return True

print("Welcome to HIGHER / LOWER Game")
time.sleep(0.5)
game()
