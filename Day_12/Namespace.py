################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local scope

# def drinkpotion():
#     potion_strength = 2
#     print(potion_strength)

# drinkpotion()
# print(portion_strength)

# Global Scope
max_health = 3 #Outside the function

def game():
    def drinkpotion():
        potion_strength = 2
        print(max_health)
    drinkpotion()

game()
print(max_health)