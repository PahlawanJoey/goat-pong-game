from turtle import Turtle
from math import ceil

ALIGNMENT = "center"
FONT = ("serif", 30, "normal")


class Screeninfo(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("saddle brown")
        self.score = 0

    def playingfield(self, x, y):
        top = y
        amount_of_lines = ceil((y * 2) / 40)
        self.fillcolor("saddle brown")
        for field in range(amount_of_lines):
            self.setpos(x, top)
            self.pendown()
            self.setheading(270)
            self.begin_fill()
            for shape in range(2):
                self.forward(20)
                self.left(90)
                self.forward(10)
                self.left(90)
            self.end_fill()
            self.penup()
            top -= 40

    def score_player(self, score_input, x_pos, y_pos):
        self.clear()
        self.setpos(x=x_pos, y=y_pos)
        self.score += score_input
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
