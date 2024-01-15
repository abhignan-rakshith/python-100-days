from turtle import Turtle
Y_AXIS = 255


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.div_line = '|'
        self.yaxis = Y_AXIS
        self.create_board()
        self.update_board()

    def create_board(self):
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        for _ in range(10):
            self.goto(0, self.yaxis)
            self.write(self.div_line, align="center", font=("Arial", 30, "normal"))
            self.yaxis -= 60
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.yaxis = Y_AXIS
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.yaxis = Y_AXIS
        self.update_board()
