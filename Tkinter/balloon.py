from tkinter import *
import random
import threading

#Move balon function
def moveBalloon(balloon: Label, speed: int) -> None:
    balloon.place(x = balloon.winfo_x() + speed, y = balloon.winfo_y() + speed)

#Stop balloon
def stopBalloon(balloon: Label) -> None:
    balloon.place(x = balloon.winfo_x(), y = balloon.winfo_y())

#Check balloon collision
def checkCollision(colX: int, colY: int, balon: Label) -> bool:
    if (balon.winfo_x() in colX) and (balon.winfo_y() in colY):
        return True
    
#Balloon pop animation
def popBalloon(imgList: list, balloon: Label, event: threading.Event,root: Tk) -> None:
    for i, j in enumerate(imgList):
        event.wait(0.5)
        changeImg = PhotoImage(file = f"Tkinter\Files\{j}.png")
        balloon.config(image = changeImg)
        root.update()

        if i == 2:
            event.wait(1)
            quit()

#Main
if __name__ == "__main__":
    #Variables
    WIDTH = 700
    HEIGHT = 500

    BALLOONSPEED = 10

    balonX = random.randrange(20, 220)
    balonY = random.randrange(20, 300)
    
    cactusX = random.randrange(320, 450)
    cactusY = random.randrange(250, 300)

    cactusHitBoxX = range(cactusX - 34, cactusX + 44)
    cactusHitBoxY = range(cactusY - 170, cactusY + 170)

    print(f"Balloon cords: [{balonX}, {balonY}]")
    print(f"Cactus cords: [{cactusX}, {cactusY}]")
    print(f"Cactus hitbox X: {cactusHitBoxX}")
    print(f"Cactus hitbox Y: {cactusHitBoxY}")

    #Thread
    event = threading.Event()

    #Root Tk
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)

    #Canvas
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    #Cactus
    cactusImg = PhotoImage(file = "Tkinter\Files\kaktus.png")
    cactus = Label(canvas, image = cactusImg)
    cactus.place(x = cactusX, y = cactusY)

    #Balloon
    balloonImages = ["balon1", "balon2", "balon3"]
    balloonImg = PhotoImage(file = f"Tkinter\Files\{balloonImages[0]}.png")
    balloon = Label(canvas, image = balloonImg)
    balloon.place(x = balonX, y = balonY)

    #First update
    root.update()

    #Mainloop
    while True:
        root.update()
        root.after(45, moveBalloon(balloon, BALLOONSPEED))

        if checkCollision(cactusHitBoxX, cactusHitBoxY, balloon):
            stopBalloon(balloon)
            popBalloon(balloonImages, balloon, event, root)

        if balloon.winfo_x() > WIDTH:
            print("The balloon didn't the cactus")
            break