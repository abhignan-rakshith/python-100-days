from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Objects for this project
paddle_r = Paddle((350, 0), "red")
paddle_l = Paddle((-350, 0), "blue")
pong = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddle_r.move_up, key="Up")
screen.onkeypress(fun=paddle_r.move_down, key="Down")
screen.onkeypress(fun=paddle_l.move_up, key="w")
screen.onkeypress(fun=paddle_l.move_down, key="s")

game_on = True
while game_on:
    screen.update()
    time.sleep(pong.move_speed)
    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # Detect collision with both paddle
    if pong.distance(paddle_r) < 50 and pong.xcor() > 320 or pong.distance(paddle_l) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    # Detect if ball exits the right screen boundary
    if pong.xcor() > 380:
        pong.reset_position()
        score_board.l_point()

    # Detect if ball exits the left screen boundary
    if pong.xcor() < -380:
        pong.reset_position()
        score_board.r_point()

screen.exitonclick()
