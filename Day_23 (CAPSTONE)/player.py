from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# TODO: 1. Create a turtle player that starts at the bottom of the screen
#  and listen for the "Up" keypress to move the turtle north.
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.color("dark khaki")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # TODO: 4. Detect when the turtle player has reached the top edge of the screen
    #  When this happens, return the turtle to the starting position and increase the speed of the cars.
    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
