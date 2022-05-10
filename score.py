from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(x=0, y=270)
        self.text()

    def text(self):
        self.write(f"Score: {self.score}", False,
                   align=ALIGN, font=FONT)

    def new_score(self):
        self.score += 1
        self.text()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGN, font=FONT)
