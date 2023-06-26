from turtle import Turtle, Screen

avia = Turtle()
screen = Screen()


def move_forwards():
    avia.forward(10)

def move_backwards():
    avia.backward(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.exitonclick()