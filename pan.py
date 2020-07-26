import turtle
import random
import time

points = 0
food = turtle.Turtle()
food.color("blue")
while True:
    food.shape("turtle")
    time.sleep(1)
    food.shape("arrow")
    time.sleep(1)
    food.shape("circle")
    time.sleep(1)
    break
food.showturtle()
food.penup()

pointurtle = turtle.Turtle

screen = turtle.Screen()
screen.screensize(400, 400)

move_speed = 12
turn_speed = 12

turtle.penup()


def forward(): turtle.forward(move_speed)


def catch():
    global points
    nearby = (abs(food.xcor() - turtle.xcor()) < 8) and (abs(food.ycor() - turtle.ycor()) < 8)
    if nearby:
        food.goto(random.randint(-400, 0), random.randint(0, 400))
        points = points + 1
        screen.title(points)


def forward():
    turtle.forward(move_speed)
    catch()


def backward():
    turtle.backward(move_speed)
    catch()


def left():
    turtle.left(turn_speed)
    catch()


def right():
    turtle.right(turn_speed)
    catch()


turtle.home()

screen.onkeypress(forward, "Up")

screen.onkeypress(backward, "Down")

screen.onkeypress(left, "Left")

screen.onkeypress(right, "Right")

screen.listen()

screen.exitonclick()
