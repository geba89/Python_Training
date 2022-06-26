#guessing game
import random
import time

def choose_difficulty(difficulty):
    diff_dict = {"easy" : 10, "medium" : 7, "hard" : 5}
    return diff_dict[difficulty]

def game():
    number_of_guesses = choose_difficulty(input("Please choose difficulty: easy / medium / hard: "))
    print("OK great! I will not think of a number between 1  and 100!")
    number_to_guess = random.randint(1,100)
    time.sleep(1.5)
    
    while number_of_guesses > 0:
        print(f"You got {number_of_guesses} guesses left.")
        guess_number = int(input("Make a guess: "))
        if guess_number == number_to_guess:
            print(f"You are right! It's {guess_number}!")
            break
        elif guess_number > number_to_guess:
            print("Wrong shot! You went to high!")
        elif guess_number < number_to_guess: 
            print("To low! Try again!")
        number_of_guesses -= 1
    
    if number_of_guesses == 0:
        print(f"You lost... try again next time! Correct number was {number_to_guess}")
    else:
        print("Congratulations! You got it!")

    play_again = input("Do you want to play again? (y / n)")

    if play_again == "y":
        game()

print("Welcome to the Number guessing game!")
game()