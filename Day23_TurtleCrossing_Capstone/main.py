from turtle import Screen
from frog import Frog
from car import Car
from level import Level
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("pink")
screen.tracer(0)

car = Car()
car.hideturtle()
frog = Frog()
level = Level()
screen.listen()
screen.onkey(frog.up, "u")


game_is_on = True
while game_is_on:
    time.sleep(0.4)
    screen.update()
    car.screen_car()
    car.move()
    if frog.ycor() > 380:
        level.update_score()
        frog.reset_t()
        car.level_up()
    for i in car.cars:
        if i.distance(frog) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()