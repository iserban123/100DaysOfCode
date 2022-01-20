from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("plum")


def draw_shape(no_sides):
    for _ in range(no_sides):
        angle = 360/no_sides
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(50)
    no_sides += 1

for x in range(3,11):
    draw_shape(x)
screen = Screen()
screen.exitonclick()
dfdf
lll
ggg
