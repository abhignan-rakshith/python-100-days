############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############### Blackjack House Rules #####################
from random import choice
import os
from art import logo

# return a random card from cards list
def deal_card():
    """This function returns a random card from cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]"""
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards):
    """This functions checks BlackJack, Replaces Ace if losing and sums up a list"""
    # BlackJack
    if sum(cards) == 21:
        print("Black Jack")
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the scores according to BlackJack Rules after the User's and Computer's turn"""
    if computer_score == 0:
        return "Lose, opponent has Blackjack :("
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score == computer_score:
        return "Draw"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "YOU WIN!"
    else:
        return "YOU LOSE :("

def play_game():
    """Recursive Function"""
    
    print(logo)
    
    # Dealing the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    game_on = True
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
          game_on = False
        else:
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == "y":
            user_cards.append(deal_card())
          else:
            game_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()