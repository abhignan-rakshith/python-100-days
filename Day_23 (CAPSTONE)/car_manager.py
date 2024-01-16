from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "cyan", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
XCOR = 300


# TODO: 2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
#  and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen.

class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_random_car(self):
        random_chance = randint(1, 6)
        if random_chance == 3:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(XCOR, randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        # print(self.car_speed)
        for car in self.car_list:
            if car.xcor() < -350:
                self.car_list.remove(car)
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
