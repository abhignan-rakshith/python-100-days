import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # Dict comprehension from a pd DataFrame


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def to_nato():
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]  # List comprehension
        print(nato_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        to_nato()


to_nato()
