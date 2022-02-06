from turtle import Turtle, Shape, Screen
from tkinter import PhotoImage
import random


class GoatBall(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.goat_img = PhotoImage(file="GOAT.gif").subsample(10, 10)
        self.screen.addshape("goat", Shape("image", self.goat_img))
        self.penup()
        self.shape("goat")
        self.x_move = 11
        self.y_move = 11
        self.game_speed = 0.04

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.setheading(0)

    def wall_bounce(self):
        self.y_move *= -1

    def player_bounce_right(self):
        self.x_move = -(abs(self.x_move))
        self.game_speed *= 0.9

    def player_bounce_left(self):
        self.x_move = abs(self.x_move)
        self.game_speed *= 0.9

    def respawn(self, direction):
        self.game_speed = 0.04
        self.setposition(0, 0)
        self.y_move = random.randint(11, 14) * direction
        self.x_move = random.randint(11, 14) * direction
