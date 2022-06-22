#hangman
import random
import Day6

Day6.hello("Piotr")

# variables
word_list = ["ardvark", "baboon", "camel"]
lifes = 6
letters = []
hit = True
lost = False
won = False

# word choice
word_to_guess = random.choice(word_list)

# create guess list
for i in word_to_guess:
    letters.append("_")

# game over check methods
def wining_check(word, guesses):
    if(word_to_guess == "".join(letters)):
        return True
    else:
        return False

def death_check(lives_left):
    if(lives_left == 0):
        return True
    else:
        return False

# print letters
print(" ".join(letters))
# main game loop
while(not won and not lost):
    # ask for letter
    print("Guess the letter: ")
    letter = input().lower()
    
    # check if we have the letter in our word
    index = 0
    for letter_in_word in word_to_guess:
        if(letter == letter_in_word):
            letters[index] = letter
            hit = False            
        index = index + 1

    # decrease lives if didnt guess the letter
    if(hit):
        lifes -= 1
        print("Uhh... not this time...")
    else:
        print("Correct! Nice guess!")

    # reset values
    index = 0
    hit = True

    # print current guesses
    print(" ".join(letters))

    # check if won/lost
    won = wining_check(word_to_guess, letters)
    lost = death_check(lifes)

# game over
if(won):
    print("Congratulations!")
else:
    print("You died....")
