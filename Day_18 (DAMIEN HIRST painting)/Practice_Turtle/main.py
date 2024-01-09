# import heroes # This is not part of the python standard library
# print(heroes.gen())

# from turtle import *
# The above code becomes confusing for larger codes
# import turtle as t
# The above code is called aliasing...as t

import turtle as t
import random as ran

t.colormode(255)
tim = t.Turtle()
tim.shape("triangle")


# # TODO: 1. Draw a 100x100 square using turtle
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# # TODO: 2. Draw a Dashed Line having 50 segments
# tim.pu()
# tim.setpos(-550, 0)
# tim.pd()
# for _ in range(50):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

# # TODO: 3. Draw triangle, square, pen, hex, hept, oct, non and decagon
# # Length of sides are 100 paces
# tim.pu()
# tim.setpos(65, 100)
# tim.pd()
# list_of_colors = ["blue", "green yellow", "gold", "deep pink", "lime", "purple", "maroon", "black", "dark slate blue"]
# for side in range(3, 11):
#     tim.color(choice(list_of_colors))
#     angle = 360 / side
#     for _ in range(side):
#         tim.right(angle)
#         tim.forward(100)

# # TODO: 4. Draw a Random Walk
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGrey", "SeaGreen"]
# def random_color():
#     r = ran.randint(0, 255)
#     g = ran.randint(0, 255)
#     b = ran.randint(0, 255)
#     my_color = (r, g, b)
#     return my_color
#
#
# list_of_coords = [90, 180, 270, 0]  # North, West, South and East
#
# tim.home()
# tim.hideturtle()
# tim.speed("fastest")
# tim.pensize(12)
#
# for _ in range(175):
#     tim.color(random_color())
#     tim.setheading(ran.choice(list_of_coords))
#     tim.forward(30)

# TODO: 5. Draw a Spirograph
def random_color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    my_color = (r, g, b)
    return my_color


tim.home()
tim.hideturtle()
tim.speed("fastest")
degree = 0
for _ in range(72):
    tim.color(random_color())
    tim.circle(150)
    degree += 5
    tim.setheading(degree)


screen = t.Screen()
screen.exitonclick()
