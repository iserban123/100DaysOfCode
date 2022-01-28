from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("pink")
screen.tracer(0)

paddle_l = Paddle((470, 0))
paddle_r = Paddle((-470, 0))
ball = Ball()


screen.listen()
screen.onkey(paddle_l.up, "p")
screen.onkey(paddle_l.down, "m")
screen.onkey(paddle_r.up, "a")
screen.onkey(paddle_r.down, "b")

game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()
    ball.move()
screen.exitonclick()