import turtle
import random

def drawBroom(broomLength: int, bristlesNum: int, bristleLength: int) -> None:
    turtle.penup()
    randX = random.randint(-50,200)
    randY = random.randint(-200, 200)
    turtle.goto(randX, randY)

    turtle.pendown()
    turtle.fd(broomLength)

    turnDegree = 45

    for i in range(bristlesNum):
        turtle.pendown()
        if i == 0:
            turtle.fd(bristleLength)
            turtle.penup()
            turtle.lt(180)
            turtle.fd(bristleLength)
            turtle.lt(180)
        else:
            turtle.lt(turnDegree)
            turtle.fd(bristleLength)


if __name__ == "__main__":
    sc = turtle.Screen()
    sc.setup(640, 480)
    turtle = turtle.Turtle()
    turtle.speed(1)
    drawBroom(100, 5, 50)