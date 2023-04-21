from turtle import *
from keyboard import is_pressed
from time import sleep

def text(string, y, size, c=0):
    pen = Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, y)
    pen.write(string, align="center", font=("Verdana", size, "bold"))
    if c:
        sleep(0.14)
        pen.clear()


def check_wall():
    if abs(ball.xcor()) > 440:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 70)
    if ball.ycor() < board.ycor() + 15 and abs(ball.xcor() - board.xcor()) < 50:
        ball.dy *= -1


def gad_check_wall():
    if ball.ycor() > 240 and abs(ball.xcor()) < 100:
        ball.dy *= -1
        text("Ай!", 210, 15, 1)



def platform_moving_up():
    x = board.xcor()
    x += 25
    if x > 440:
        x = 440
    board.setx(x)


def platform_moving_down():
    x = board.xcor()
    x -= 20
    if x < -350:
        x = -350
    board.setx(x)


def platform_moving():
    win.listen()
    win.onkeypress(platform_moving_up, "Right")
    win.onkeypress(platform_moving_down, "Left")


def ball_moving():
    pass


win = Screen()
win.title("Destroy him!")
win.bgcolor("black")
win.setup(width=900, height=600)
win.tracer(0)

board = Turtle()
board.speed(0)
board.shape("square")
board.color("blue")
board.shapesize(stretch_len=5, stretch_wid=0.6)
board.penup()
board.goto(0, -260)
platform_moving()

ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.shapesize(1)
ball.penup()
ball.goto(0, 70)
ball.dx = ball.dy = 0.25

text("Босс", 260, 24)

while True:
    win.update()
    if is_pressed('ESc'):
        break
    check_wall()
    gad_check_wall()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
