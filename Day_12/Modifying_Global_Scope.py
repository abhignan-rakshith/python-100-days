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
# max_health = 3 #Outside the function

# def game():
#     def drinkpotion():
#         potion_strength = 2
#         print(max_health)
#     drinkpotion()

# game()
# print(max_health)

# THERE IS NO BLOCK SCOPE IN PYTHON
# game_lvl = 3
# def create_enemy():
#     enemies = ["Skeletons", "Zombies", "Spiders"]
#     if game_lvl < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)
# # print(new_enemy)

# # Modifying Global Scope (Not recommended)
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Instead Use this:
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants (upper case)

PI = 3.14159
URL = "https://google.com"
TWITTER_HANDLE = "@Abhi_Rakz"