# # Importing turtle module
# import turtle
#
# # Tapping into the turtle module with '.' operator and accessing Turtle 'Class' (PascalCasing), initialized it with '()'
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('SeaGreen2')
#
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Packages: They differ from modules as it is a bunch of code aim at achieving a single purpose, all 'packaged' together
# File->Settings->project->project interpreter->+

# right-click->goto->implementations
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
