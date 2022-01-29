from turtle import Turtle
from frog import Frog
colors = ["red", "yellow", "blue", "green", "orange", "black"]
#pos = [(450, 0), (400, 50), (350, 100)]

import random

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 30

    def screen_car(self):
        chance = random.randint(1,6)
        if chance == 1:
          for i in range(random.randint(1,6)):
              carx = Turtle()
              carx.shapesize(1, 3)
              carx.color(random.choice(colors))
              carx.penup()
              carx.shape("square")
              x = 400 + random.randrange(0, 60, 20)
              y = -300 + random.randrange(0, 600 , 50)
              carx.goto(x, y)
              self.cars.append(carx)


    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def level_up(self):
            self.car_speed += 10





