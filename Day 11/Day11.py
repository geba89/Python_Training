import random
import time
from tabnanny import check

cards = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11
}

def get_card():
    return random.choice(list(cards))

def check_score(score):
    if score > 21:
        return True
    else:
        return False

def play_game():  
    latest_card = ""  
    pc_score = 0
    player_score = 0
    player_loop = True
    pc_loop = True
    over = False

    latest_card = get_card()
    pc_score = cards[latest_card]

    time.sleep(1)
    print(f"I have drawn {latest_card} which is {pc_score} points.")

    time.sleep(1)
    print("I will draw for you now.")
    latest_card = get_card()
    time.sleep(1)
    print(f"Your card is {latest_card} which is {cards[latest_card]} points")
    player_score += cards[latest_card]
    latest_card = get_card()
    time.sleep(1)
    print(f"Your second card is {latest_card} which is {cards[latest_card]} points")
    player_score += cards[latest_card]

    while player_loop and not over:
        time.sleep(1)
        print(f"Your current score is {player_score}")
        play = input("Do you want to draw next card? (y/n)")
        time.sleep(1)
        if play == "y":
            latest_card = get_card()
            if latest_card == "A" and player_score > 10:
                player_score += 1
                print(f"Your card is {latest_card} which in this case will be worth {1} point")
            else:
                print(f"Your card is {latest_card} which is {cards[latest_card]} points")
                player_score += cards[latest_card]

            over = check_score(player_score)
            if player_score == 21:
                print("Black Jack!")
                player_loop = False
            elif player_score > 21:
                print("To high!")
                player_loop = False
        else:
            player_loop = False
    
    if over:
        print(f"You lost... you got over 21 points.")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            play_game()
        return

    while pc_loop and not over:
        time.sleep(1)
        print(f"My current score is {pc_score}")      
        time.sleep(1)  
        if player_score > pc_score:
            latest_card = get_card()
            if latest_card == "A" and pc_score > 10:
                pc_score += 1
                print(f"My card is {latest_card} which in this case will be worth {1} point")
            else:                
                pc_score += cards[latest_card]            
                print(f"My card is {latest_card} which is {cards[latest_card]} points")
            
            over = check_score(pc_score)
            if pc_score == 21:
                print("Black Jack!")
                pc_loop = False
            elif pc_score > 21:
                print("To high!")
                pc_loop = False
        else:
            pc_loop = False
    time.sleep(1)
    if over:
        print(f"You won! Congratulations! You beat me with {player_score}!")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            play_game()
        return
    else:
        print(f"I won with score of {pc_score}.")
        time.sleep(0.5)
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            play_game()
        return


print("Welcomce to Black Jack")

play_game()