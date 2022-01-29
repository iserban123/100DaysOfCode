from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.reset()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=-20, y=260)
        self.pendown()
        self.y = 0
        self.high_score = self.y
        self.new_score()

    def new_score(self):
        self.clear()
        self.write(f"Score: {self.y}, High Score: {self.high_score} ", font=FONT)


    def update_score(self):
        self.y += 1
        self.new_score()

    def game_over(self):
        if self.y > self.high_score:
            self.high_score = self.y
        self.y = 0
        self.new_score()






