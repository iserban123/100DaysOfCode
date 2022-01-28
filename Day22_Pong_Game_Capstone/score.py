from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto(0, 340)
        self.update_score()

    def set_score_r(self):
        self.l_score += 1

    def set_score_l(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}:{self.r_score}", font=("Arial", 25, "normal"))
