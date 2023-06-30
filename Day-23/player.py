from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
