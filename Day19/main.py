from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()

def move_fw():
    tim.forward(50)

def move_bw():
    tim.backward(50)

def move_clockw():
    tim.right(10)

def move_cc():
    tim.left(10)

def clear_s():
    tim.clear()

screen.onkey(move_fw, "a")
screen.onkey(move_bw, "b")
screen.onkey(move_clockw, "c" )
screen.onkey(move_cc, "d" )
screen.onkey(clear_s, "w" )

screen.exitonclick()
