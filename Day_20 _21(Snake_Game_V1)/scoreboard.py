from turtle import Turtle

POSITION = (0, 270)
ALIGN = "center"
FONT = ('Apple Chancery', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.score = 0
        self.red = 0
        self.green = 255
        self.update_score()

    def update_score(self):
        if self.red < 250:
            self.color(self.red, self.green, 0)
            self.green -= 10
            self.red += 10
        else:
            self.color(0, 0, 255)

        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
