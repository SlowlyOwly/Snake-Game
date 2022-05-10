from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randrange(-260, 260, 20),
                  y=random.randrange(-260, 260, 20))
