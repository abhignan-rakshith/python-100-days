import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # Dict comprehension from a pd DataFrame

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_list = [char for char in user_input]  # List comprehension

nato_list = [nato_dict[letter] for letter in user_list if letter in nato_dict]  # List comprehension

print(nato_list)
