import turtle

def drawBroom(broomLength: int, bristlesNum: int, bristleLength: int) -> None:
    turtle.fd(broomLength)

    for _ in range(bristlesNum):
        turtle.pendown()
        turtle.lt(25)
        turtle.fd(bristleLength)
        turtle.penup()
        turtle.lt(180)
        turtle.fd(bristleLength)
        turtle.lt(180)

if __name__ == "__main__":
    turtle = turtle.Turtle()
    turtle.speed(1)
    drawBroom(100, 5, 50)