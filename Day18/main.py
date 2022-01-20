from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("plum")

timmy_the_turtle.forward(50)
x = 3
while x <= 10:
    for i in range(x):
        print(x)
        y = 180 - ((x - 2) * 180)/x
        print(y)
        timmy_the_turtle.right(y)
        timmy_the_turtle.forward(50)
    x += 1
screen = Screen()
screen.exitonclick()
