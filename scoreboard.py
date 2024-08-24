from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.move_speed = 0.1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def score_point(self):
        self.score += 1
        self.move_speed *= 0.9
        self.update_scoreboard()
        print(round(self.move_speed, 2))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)

        