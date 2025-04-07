from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        # x_position = random.randint(-280,280)
        # y_position = random.randint(-280,280)
        #
        # self.goto(x_position,y_position)
        self.refresh()

    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)

        self.goto(x_position, y_position)
