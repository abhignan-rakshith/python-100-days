from turtle import Turtle

FONT = ("Courier", 24, "normal")


# TODO: 5. Create a scoreboard that keeps track of which level the user is on.
#  Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.create_board()
        self.update_board()

    def create_board(self):
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_board(self):
        self.clear()
        self.goto(-290, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
