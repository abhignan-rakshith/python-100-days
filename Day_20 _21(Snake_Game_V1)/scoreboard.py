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
        with open(file="data.txt", mode='r') as data:
            self.highscore = int(data.read())
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
        self.write(arg=f"Score: {self.score}   High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file="data.txt", mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.red = 0
        self.green = 255
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(arg="GAME OVER", align=ALIGN, font=FONT)
