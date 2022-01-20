import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
#angle = [-90,0,90,180]
timmy_the_turtle = Turtle()
timmy_the_turtle.color("pink")
timmy_the_turtle.speed(0)

def color_change():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color_tuple = (r, g, b)
  return color_tuple


def my_rotate(y):
  for _ in range(int(360/y)):
    timmy_the_turtle.color(color_change())
    timmy_the_turtle.circle(200)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + y)

#for i in range(200,100,-25):
  #  timmy_the_turtle.color(color_change())
my_rotate(15)
#TODO program care sa deseneze mandala



#timmy_the_turtle.speed(8)
#timmy_the_turtle.pensize(10)




#for _ in range(200):
# timmy_the_turtle.color(color_change())
# timmy_the_turtle.forward(20)
# timmy_the_turtle.right(random.choice(angle))


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