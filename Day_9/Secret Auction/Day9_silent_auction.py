import os
from art import logo

more_bidders = True

def find_highest_bidder(bid_record):
    max_key = max(bid_record, key=bid_record.get)
    max_value = bid_record[max_key]
    print("The winner is {} with a bid of ₹{}.".format(max_key, max_value))
    

print(logo)

print("\nWelcome to the silent auction program.")

auction = {}
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: ₹"))
    
    auction[name] = bid

    anymore = input("\nAre there anymore bidders. Type 'yes' or 'no'.\n")
    os.system('cls')
    print(logo)
    if anymore == 'no':
        more_bidders = False
        find_highest_bidder(bid_record=auction)

w = input("\nPress 'enter' to exit ...")