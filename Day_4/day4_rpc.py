from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# My code below this line 👇

game_images = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_input > 2 or user_input < 0:
    print("Please input a VALID number...exiting program...!!!\n")
else:
    print(game_images[user_input])
    computer_input = randint(0, 2)
    print(game_images[computer_input])
    if computer_input == user_input:
        print("It's a Draw...")
    else:
        if user_input == 0:
            if computer_input == 1:
                print("You Lose...:(")
            else:
                print("You Win!!!")
        elif user_input == 1:
            if computer_input == 0:
                print("You Win!!!")
            else:
                print("You Lose...:(")
        else:
            if computer_input == 0:
                print("You Lose...:(")
            else:
                print("You Win!!!")
