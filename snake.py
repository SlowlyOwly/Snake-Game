from turtle import Turtle, Screen

screen = Screen()


class Snake:

    def __init__(self):
        self.segments = []
        self.body()
        self.head = self.segments[0]

    def body(self):

        snake_body = 2
        pos_x = 0
        pos_y = 0

        for segment in range(snake_body):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.speed(1)
            new_segment.penup()
            new_segment.setposition(x=pos_x, y=pos_y)
            pos_x -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].setposition(new_x, new_y)
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() == 270:
            self.head.seth(270)
        else:
            self.head.seth(90)

    def turn_down(self):
        if self.head.heading() == 90:
            self.head.seth(90)
        else:
            self.head.seth(270)

    def turn_left(self):
        if self.head.heading() == 0:
            self.head.seth(0)
        else:
            self.head.seth(180)

    def turn_right(self):
        if self.head.heading() == 180:
            self.head.seth(180)
        else:
            self.head.seth(0)

    def add_segment(self):
        last_pos = self.segments[-1].position()
        add = Turtle(shape="square")
        add.color("white")
        add.speed(1)
        add.penup()
        add.goto(last_pos)
        self.segments.append(add)
