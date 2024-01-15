from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, colour):
        super().__init__()
        self.create_paddle(position, colour)

    def create_paddle(self, coords, color):
        self.shape("square")
        self.penup()
        self.color(color)
        self.turtlesize(1, 5)
        self.goto(coords)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
