from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(-450, 360)
        self.lev = 1
        self.update_score()

    def set_level(self):
        self.lev += 1

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.lev}", font=("Arial", 20, "normal"))
        self.set_level()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", font=("Arial", 40, "normal"))



