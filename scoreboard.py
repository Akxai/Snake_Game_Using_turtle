from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
file = open("../pythonProject1/data.txt", "r")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../pythonProject1/data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../pythonProject1/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
