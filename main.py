from turtle import Screen
from screeninfo import Screeninfo
from players import Player
from goatball import GoatBall
import time

keys_pressed = {}
screen = Screen()
screen.setup(width=1200, height=670)
screen.title("GOAT PONG")
screen.bgcolor("navajo white")
screen.tracer(0)
screeninfo = Screeninfo()
playingfield = screeninfo.playingfield(x=-5, y=screen.window_height() // 2)
pscore1 = Screeninfo()
pscore2 = Screeninfo()
score_player1 = 0
score_player2 = 0
pscore1.score_player(score_input=score_player1, x_pos=(screen.window_width() // 2 * -1) + 300,
                     y_pos=(screen.window_height() // 2 - 70))
pscore2.score_player(score_input=score_player2, x_pos=screen.window_width() // 2 - 300,
                     y_pos=(screen.window_height() // 2 - 70))


def pressed(event):
    keys_pressed[event.keysym] = True


def released(event):
    keys_pressed[event.keysym] = False


def key_binds():
    for key in ["w", "s", "Up", "Down"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


player1 = Player()
player1.playerposition(x=((screen.window_width() // 2) * -1) + 50, y=0)
player2 = Player()
player2.playerposition(x=(screen.window_width() // 2) - 50, y=0)
goatball = GoatBall()

exception = True
game_on = True
screen.listen()
key_binds()
while game_on:
    time.sleep(goatball.game_speed)
    goatball.move_ball()
    if goatball.ycor() > (screen.window_height() // 2) - 50 or goatball.ycor() < (
            screen.window_height() // 2) * -1 + 50:
        goatball.wall_bounce()
    if goatball.distance(player1.pos()) < 60 and goatball.xcor() > ((screen.window_width() // 2) * -1) + 45:
        goatball.player_bounce_left()
    if goatball.distance(player2.pos()) < 60 and goatball.xcor() < (screen.window_width() // 2) - 45:
        goatball.player_bounce_right()
    if goatball.xcor() > screen.window_width() // 2:
        score_player1 += 1
        pscore1.score_player(score_input=1, x_pos=(screen.window_width() // 2 * -1) + 300,
                             y_pos=(screen.window_height() // 2 - 70))
        goatball.respawn(-1)
    if goatball.xcor() < screen.window_width() // 2 * -1:
        score_player2 += 1
        pscore2.score_player(score_input=1, x_pos=screen.window_width() // 2 - 300,
                             y_pos=(screen.window_height() // 2 - 70))
        goatball.respawn(1)
    if not player1.ycor() >= screen.window_height() // 2 - 20:
        if keys_pressed["w"]: player1.moveplayerup()
    if not player1.ycor() <= (screen.window_height() // 2) * -1 + 30:
        if keys_pressed["s"]: player1.moveplayerdown()
    if not player2.ycor() >= screen.window_height() // 2 - 20:
        if keys_pressed["Up"]: player2.moveplayerup()
    if not player2.ycor() <= (screen.window_height() // 2) * -1 + 30:
        if keys_pressed["Down"]: player2.moveplayerdown()
    screen.update()
screen.exitonclick()
