from turtle import Turtle
import pandas
class Route(Turtle):
    def __init__(self):
        super().__init__()
        self.state_data = ""
        self.x_data = ""
        self.y_data = ""
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()






    def position1(self):
        data = pandas.read_csv("50_states.csv")
        self.state_data = data["state"].to_list()
        self.x_data = data["x"].to_list()
        self.y_data = data["y"].to_list()
