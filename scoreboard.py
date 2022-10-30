from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.ht()
        self.penup()
        self.setposition(0, 285)
        self.color("white")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score} Lives: {self.lives}  High score: {self.high_score}", align="center", font=("Comic Sans", 8, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.display_score()


