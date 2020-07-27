import turtle
import random
import time

turtle.screensize(600, 600)
points = 0

# BORDER
bor = turtle.Turtle()
bor.hideturtle()
bor.penup()
bor.goto(-300, 0)
bor.pendown()
bor.left(90)
bor.forward(300)
bor.right(90)
bor.forward(600)
bor.right(90)
bor.forward(600)
bor.right(90)
bor.forward(600)
bor.right(90)
bor.forward(300)

# FOOD START
food = turtle.Turtle()
food.color("blue")
food.goto(100, 100)
while True:
    food.shape("turtle")
    time.sleep(0.4)
    food.shape("arrow")
    time.sleep(0.2)
    food.shape("circle")
    time.sleep(0.3)
    break

food.penup()

screen = turtle.Screen()
screen.screensize(400, 400)

move_speed = 12
turn_speed = 12

turtle.penup()


# FOOD CATCH
def catch():
    global points
    nearby = (abs(food.xcor() - turtle.xcor()) < 12) and (abs(food.ycor() - turtle.ycor()) < 12)
    if nearby:
        food.goto(random.randint(-200, 0), random.randint(0, -200))
        points = points + 1
        screen.title(points)


# CONTROLS
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
