from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("saddle brown")
        self.shapesize(stretch_wid=1, stretch_len=3)

    def playerposition(self, x, y):
        self.setpos(x, y)

    def moveplayerup(self):
        self.forward(30)

    def moveplayerdown(self):
        self.backward(30)
