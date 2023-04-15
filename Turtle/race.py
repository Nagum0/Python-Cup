import turtle
import time
import random

#Main turtle
class MainTurtle(turtle.Turtle):
    def __init__(self, shape: str = "arrow", visible: bool = True) -> None:
        super().__init__(shape, visible)

        #Setup
        self.penup()
        self.speed(1)

        #Vars
        self.finishX = 350
        self.finishY = 325
        self.tDistance = 0

    #Start race countdown
    def startRace(self):
        self.penup()
        timeCounter = 4

        while timeCounter >= 0:
            if timeCounter == 4:
                self.write("Race start!", align="center", font=("Cooper Black", 60, "bold"))
                timeCounter -= 1
            else:
                self.write(timeCounter, align="center", font=("Cooper Black", 60, "bold"))
                timeCounter -= 1

            time.sleep(1)
            self.clear()

    #Draw finish line
    def drawFinishLine(self):
        self.penup()
        self.color("black")
        self.pensize(7)
        self.goto(self.finishX, self.finishY)
        self.rt(90)

        for i in range(25):
            if i % 2 == 0:
                self.pendown()
                self.fd(25)

            self.penup()
            self.fd(25)

    #Check winner method
    def checkWin(self, distanceList: list) -> bool:
        for i in distanceList:
            if i > self.tDistance:
                self.tDistance = i
        
        if self.tDistance > 350:
            print(self.tDistance)
            return True
        
        return False

#Race turtle
class RaceTurtle(turtle.Turtle):
    def __init__(self, shape: str = "turtle", visible: bool = True) -> None:
        super().__init__(shape, visible)

        #Setup
        self.speed(1)
    
    def drawRacer(self, x: int, y: int, name: str, mainColor: str):
        self.penup()
        self.goto(x, y)
        self.write(name, font=("Cooper Black", 15))
        self.color(mainColor)

#Main screen setup
screen = turtle.Screen()
screen.setup(1000, 650)

#Racer list
racerList = []

#Racerpos
xPos = -300
yPos = -200

#Racer setup info
racerSetup = [
    [
        "Samu",
        "red"
    ],
    [
        "Balint",
        "yellow"
    ],
    [
        "Levente",
        "black"
    ]
]

#Racer distance list
racerDistance = []

#Main
if __name__ == "__main__":
    #Init turtle
    mainTurtle = MainTurtle()
    #Start race
    mainTurtle.startRace()
    #Draw finish line
    mainTurtle.drawFinishLine()

    #Init 3 race turtles
    for i in range(3):
        racer = RaceTurtle()
        racer.drawRacer(xPos, yPos, racerSetup[i][0], racerSetup[i][1])
        yPos += 200
        racerList.append(racer)
        racerDistance.append(xPos)

    #Race loop
    while True:
        randRacer = random.randrange(0, len(racerList))
        randX = random.randrange(10, 15)
        
        racerList[randRacer].pendown()
        racerList[randRacer].pensize(5)
        racerList[randRacer].fd(randX)
        racerDistance[randRacer] += randX

        if mainTurtle.checkWin(racerDistance):
            time.sleep(5)
            break