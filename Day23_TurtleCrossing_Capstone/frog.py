from turtle import Turtle


class Frog(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shapesize(1.5, 1.5)
        self.setheading(90)
        self.penup()
        self.goto(0, -350)
        self.shape("turtle")

    def up(self):
        y = self.ycor() + 40
        self.goto(0, y)

    def reset_t(self):
        self.goto(0, -350)


