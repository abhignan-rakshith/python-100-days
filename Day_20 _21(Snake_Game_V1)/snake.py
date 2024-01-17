from turtle import Turtle

# Initializing all constants
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        # Any kind of functionality is moved into a method
        self.create_snake()  # Happens only once
        self.head = self.segments[0]  # Creating the head of the snake

    def create_snake(self):
        for cords in STARTING_POS:
            self.add_segment(cords)

    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.penup()
        snake_body.color("dark olive green")
        snake_body.goto(position)
        self.segments.append(snake_body)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # adds a new segment to the snake
        self.add_segment(position=self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
