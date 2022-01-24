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
        self.new_score()

    def new_score(self):
        self.write(f"Score: {self.y}", font=FONT)


    def update_score(self):
        self.y += 1
        self.clear()
        self.new_score()

    def game_over(self):
        self.penup()
        self.setposition(-30, 0)
        self.write(f"GAME OVER", font=FONT)






