# Password Generator Project
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = ''
for i in range(nr_letters):
    random_letters += random.choice(letters)

random_symbols = ''
for i in range(nr_symbols):
    random_symbols += random.choice(symbols)

random_numbers = ''
for i in range(nr_numbers):
    random_numbers += random.choice(numbers)

password = random_letters + random_symbols + random_numbers
print(password)

# Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_password = [*password]
print(list_password)

random.shuffle(list_password)
shuffled_password = ''
shuffled_password = shuffled_password.join(list_password)

print(shuffled_password)