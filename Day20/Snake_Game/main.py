from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#TODO remake snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "a")
screen.onkey(snake.down, "b")
screen.onkey(snake.left, "c")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 :
        score.game_over()
        score.write_hi_score()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            score.write_hi_score()
            snake.reset()



screen.exitonclick()
