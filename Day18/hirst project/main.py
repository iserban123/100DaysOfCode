import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg',10)
# print(colors)
# col_list = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    col_list.append(new_color)
# print(col_list)
color_list = [(234, 234, 233), (221, 173, 3), (2, 133, 195), (229, 116, 153), (6, 149, 98), (240, 123, 45), (243, 236, 241), (128, 160, 203), (241, 161, 189), (223, 234, 242)]


def color_line():
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

def turtle_draw(y,x):
     y_pos = y
     for i in range(10):
         tim.penup()
         tim.setpos(x, y_pos)
         color_line()
         y_pos -= 40


tim = Turtle()
screen = Screen()
screen.setup (width=2000, height=2000, startx=0, starty=0)
turtle_draw(150, -350)

screen = Screen()
screen.exitonclick()