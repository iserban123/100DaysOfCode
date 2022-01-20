from turtle import Turtle, Screen
import random

colors = ["black", "red", "purple", "yellow", "blue", "orange"]
angle = [90, -90]
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("plum")

for _ in range(50):
 timmy_the_turtle.pen(pensize=10, pencolor=random.choice(colors))
 timmy_the_turtle.forward(random.randint(10,110))
 timmy_the_turtle.right(random.choice(angle))


#def draw_shape(no_sides):
 #   for _ in range(no_sides):
 #       angle = 360/no_sides
 #      timmy_the_turtle.right(angle)
 #     timmy_the_turtle.forward(50)
 #no_sides += 1

#for x in range(3,11):
#    timmy_the_turtle.pen(pensize=10, pencolor=random.choice(colors))
#    draw_shape(x)

screen = Screen()
screen.exitonclick()