from turtle import Turtle, Screen
from random import randint

scr = Screen()
scr.register_shape('bug', ((0, 0), (3, 0), (5, 2), (3, 4), (0, 4), (-2, 2), (0, 0), (-2, -2), (0, -4), (3, -4), (5, -2), (3, 0)))


# Using inheritance to create the food turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("bug")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
