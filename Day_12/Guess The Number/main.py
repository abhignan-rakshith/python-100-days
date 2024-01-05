# ASCII art from:
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

#import sys
from random import randint
from time import sleep
from art import logo

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY = 10
HARD = 5


def compare_nums(user_guess, random_num, life):
    """Compares the two numbers"""
    if user_guess > random_num:
        print("Too High.")
        print("Guess Again.")
        return life - 1
    elif user_guess < random_num:
        print("Too Low")
        print("Guess Again.")
        return life - 1
    else:
        print(f"You Got It! The answer was {random_num}.")
        #sys.exit(0)
        life = -1
        return life 
        
    
def calc_lives(option):
    """Calculates 'lives' variable"""
    if option == 'hard':
        return HARD
    return EASY


# Include an ASCII art logo.
print(logo)
def game(): 
    sleep(1)
    print("Welcome to the number Guessing Game!")
    sleep(1)
    print("I'm thinking of a number between 1 and 100...")
    sleep(2)
    random_int = randint(1, 100)
    print(random_int)

    # Allow the player to submit a guess for a number between 1 and 100.
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = calc_lives(level)
    
    game_on = True
    while game_on:
        print(f"You have {lives} lives remaining to guess the number.\n")
        guess = int(input("Make a Guess ---> "))
        
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
        # If they got the answer correct, show the actual answer to the player.
        lives = compare_nums(user_guess=guess, random_num=random_int, life=lives)
    
        # Track the number of turns remaining.
        # If they run out of turns, provide feedback to the player. 
        if lives == 0:
            print("You've run out of guesses. You Lose.")
            game_on = False
        elif lives == -1:
            game_on = False
        
game()