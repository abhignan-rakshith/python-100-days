import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("midnight blue")
screen.title("TURTLE CROSSING")
screen.tracer(0)

# Objects created in project
player1 = Player()
car_control = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player1.move_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_control.generate_random_car()
    car_control.move_cars()

    # TODO: 3. Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_control.car_list:
        if player1.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # check if player1 reached the finish line and update scoreboard
    if player1.is_at_finish():
        player1.go_to_start()
        car_control.increase_car_speed()
        score_board.update_board()

screen.exitonclick()
