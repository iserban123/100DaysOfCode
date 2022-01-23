from turtle import Turtle
MOVE=10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.ypos = 0
        self.xpos = 0
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setposition(x=self.xpos, y=self.ypos)
            self.xpos += MOVE
            self.snake_segments.append(snake)

    def move(self):
        for snake_segment in range(len(self.snake_segments) - 1, 0, -1):
            x_new = self.snake_segments[snake_segment-1].xcor()
            y_new = self.snake_segments[snake_segment - 1].ycor()
            self.snake_segments[snake_segment].goto(x_new, y_new)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
             self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)










