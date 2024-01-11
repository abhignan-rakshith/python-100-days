# Created by abhignan-rakshith at 11:18 am 11-01-2024 using PyCharm
# Learnt the concept of Higher Order Functions
# Learnt about instances and states of a given object

from turtle import Turtle, Screen
from random import shuffle, randint

# # TODO: 1. Make an Etch-A-Sketch program
# tim = Turtle()
# tim.speed("fastest")
# screen = Screen()


# def move_forwards():
#     tim.color("lime")
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.color("red")
#     tim.backward(10)
#
#
# def clockwise():
#     tim.color("blue")
#     tim.right(10)
#
#
# def anti_clockwise():
#     tim.color("yellow")
#     tim.left(10)
#
#
# def clear_screen():
#     tim.home()
#     tim.clear()
#
#
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=anti_clockwise)
# screen.onkeypress(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.listen()

# TODO: 2. Make an Turtle Racing Game
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "yellow", "orange", "green", "blue", "purple"]
shuffle(colors)  # Giving each turtle a unique start point every race

all_turtles = []
y_coords = 150

for color in colors:
    y_coords -= 45
    new_turtle = Turtle(shape="turtle")
    # tim.speed("fastest")
    new_turtle.color(color)
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_coords)
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make you bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner...")
            is_race_on = False
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
