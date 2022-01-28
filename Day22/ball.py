from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.speed(3)
        self.color("red")
        #self.move_ball()


    def move(self):
        angle = random.randint(0,360)
        self.right(angle)
        x = 0
        y = 0
        x += 10
        y += 10
        self.goto(x,y)









