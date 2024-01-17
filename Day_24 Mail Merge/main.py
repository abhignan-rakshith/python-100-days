# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open(file="./Input/Names/invited_names.txt") as name_data:
    name_list = name_data.readlines()

with open(file="./Input/Letters/starting_letter.txt") as letter_data:
    letter_list = letter_data.read()
    for name in name_list:
        strip_name = name.strip()
        new_letter = letter_list.replace("[name]", strip_name)
        with open(file=f"./Output/ReadyToSend/{strip_name}.txt", mode='w') as rts_letter:
            rts_letter.write(new_letter)
