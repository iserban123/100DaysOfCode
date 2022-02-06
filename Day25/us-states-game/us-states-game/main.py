import turtle

import pandas

screen = turtle.Screen()
screen.title("US States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turt = turtle.Turtle()

states = pandas.read_csv("50_states.csv")
all_states = states["state"]

x=0
gameon = True
while gameon:
    answer = screen.textinput(title=f"Guess the State {x}/50", prompt="What'S another state's name")
    for st in all_states:
        if st.lower() == answer.lower():
            x_c = float(states[all_states == st]["x"])
            y_c = float(states[all_states == st]["y"])
            print(x_c, y_c)
            turt.hideturtle()
            turt.penup()
            turt.goto(x_c, y_c)
            turt.pendown()
            turt.write(st)
            x += 1
            if x == 50:
                gameon = False
                print("you won")








# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()