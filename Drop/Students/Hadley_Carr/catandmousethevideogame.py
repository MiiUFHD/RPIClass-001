import turtle
import time

boxsize = 200
caught = False
score = 0

def up():
    mouse.forward(10)
    checkbound()


def back():
    mouse.backward(10)
    checkbound()
    

def left():
    mouse.left(45)

def right():
    mouse.right(45)

def quitTurtles():
    window.bye()

def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    

    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)

window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100,100)


window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window
