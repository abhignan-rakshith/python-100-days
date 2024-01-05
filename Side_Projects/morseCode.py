# Morse Code Algorithm to Encrypt/ Decrpt a message
import os

#ASCII art
logo = '''___  ______________  _____ _____   _____ ___________ _____  
|  \/  |  _  | ___ \/  ___|  ___| /  __ \  _  |  _  \  ___| 
| .  . | | | | |_/ /\ `--.| |__   | /  \/ | | | | | | |__   
| |\/| | | | |    /  `--. \  __|  | |   | | | | | | |  __|  
| |  | \ \_/ / |\ \ /\__/ / |___  | \__/\ \_/ / |/ /| |___  
\_|  |_/\___/\_| \_|\____/\____/   \____/\___/|___/ \____/  
                                                            
                                                            '''

MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  

# Dictionary Comprehension
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Using .join() method to get a string
def encrypt(message: str) -> str:
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())


def decrypt(message: str) -> str:
    return "".join(REVERSE_DICT[char] for char in message.split())


if __name__ == "__main__":
    go_again = True
    while go_again:
        print(logo)
        cipher = input("Type 'e' to encrypt OR Type 'd' to decrypt: ")
        if cipher == 'e':
            message = input("What's the plain text: ")
            message = encrypt(message)
            print(message)
        elif cipher == 'd':
            message = input("What's the cipher text: ")
            message = decrypt(message)
            print(message)
        else:
            print("Bad Command...exiting--->")
            
        again = input("Go Again? 'y'/'n': ")
        if again == 'y':
            os.system('cls')
        else:
            go_again = False
            os.system('cls')
            print("GoodBye!")
            w = input("Hit 'enter to exit...'")
            
