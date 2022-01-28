from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("pink")
screen.tracer(0)

paddle_r = Paddle((470, 0))
paddle_l = Paddle((-470, 0))
ball = Ball()
sc = Score()



screen.listen()
screen.onkey(paddle_l.up, "p")
screen.onkey(paddle_l.down, "m")
screen.onkey(paddle_r.up, "a")
screen.onkey(paddle_r.down, "b")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.bounce_y()
    if (ball.xcor() > 430 and ball.distance(paddle_r) < 50) or (ball.xcor() < -430 and ball.distance(paddle_l) < 50) :
        ball.bounce_x()
    if ball.xcor() > 480:
        sc.set_score_r()
        sc.update_score()
        ball.reset_pos()
        ball.bounce_x()
    if ball.xcor() < -480:
        sc.set_score_l()
        sc.update_score()
        ball.reset_pos()
        ball.bounce_x()

screen.exitonclick()