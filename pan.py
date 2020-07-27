import turtle
import random
import time
from numpy import sign

turtle.screensize(600, 600)
points = 1
turtle.turtlesize(1)
# BORDER
bor = turtle.Turtle()
bor.color("blue")
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
food.color("green")
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
screen.screensize(600, 600)

move_speed = 12
turn_speed = 12

turtle.penup()
screen.bgcolor("lightgreen")

# FOOD CATCH
def catch():
    global points

    x = turtle.xcor()
    y = turtle.ycor()
    x = sign(x)*300 if abs(x)>300 else x
    y = sign(y) * 300 if abs(y) > 300 else y
    turtle.goto(x,y)
    nearby = (abs(food.xcor() - turtle.xcor()) < 12) and (abs(food.ycor() - turtle.ycor()) < 12)
    if nearby:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        print('going to',x,y)
        food.goto(x,y )
        points = points + 1
        turtle.turtlesize(points)


bor.color('orange')
style = ('Courier', 30, 'italic')
bor.write('POINTS:', points, font=style, align='right')

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