from os import system
from random import choice
from art import logo, vs
from game_data import data
#global score
score = 0

def random_account():
    """Get data from random account"""
    return choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    celeb = account['name']
    bio = account['description']
    location = account['country']
    return f"{celeb}, {bio}, from {location}."
    
def check_answer(guess, a_account, b_account):
    """Checks followers against user's guess"""
    if a_account > b_account:
        return guess=='A'
    else:
        return guess=='B'
    
def game():
    global score #This is done so score does not reset
    game_on=True
    accA = random_account()
    accB = random_account()
    
    while game_on:
        fcA = accA['follower_count']
        fcB = accB['follower_count']
        #Same Follower Count?
        if fcA == fcB:
            w = input("Same Accounts were generated! Press 'ENTER'...")
            game()
            
        print(logo)
        #Skip first time
        if score != 0:
            print(f"You're right! Current score: {score}.")
            
        print(f"Compare A: {format_data(accA)}")
        print(vs)
        print(f"Against B: {format_data(accB)}")
        #print(fcA, fcB).
        user_guess = input("Who has more followers? Type 'A' or 'B':").upper() #User Guess
        is_correct = check_answer(user_guess, fcA, fcB)
        if is_correct:
            score += 1
            system('cls')
            accA = accB
            accB = random_account()
        else:
            system('cls')
            print(f"Sorry, that's wrong. Final score: {score}")
            return
    
game()
w = input("Press 'ENTER' to exit...")
