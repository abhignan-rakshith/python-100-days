# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ["apples", "mangoes"]
# fruit = fruit_list[3]

# TypeError
# my_string = "Hello World!"
# print(my_string+2)

# Using try, except(not BARE), else, finally, raise

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open(file="a_file.txt", mode='w')
#     file.write("There was an error!")
# except KeyError as error_message:
#     print(f"there was a key {error_message} error!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is a KR!")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
