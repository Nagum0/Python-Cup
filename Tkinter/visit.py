from tkinter import *
import random

#Canva class
class MainCanvas(Canvas):
    def __init__(self, master: Tk, width: int, height: int):
        super().__init__(master, width=width, height=height)
        #Variables
        self.x = 0
        self.y = height - 50

        #Init bug object -> label
        self.bug = Bug(self, "Tkinter\Files\chrobacik.png", width, height)
        print(self.bug.randX, self.bug.randY)

        #Init player -> ladybug
        self.playerImg = PhotoImage(file="Tkinter\Files\lienka.png")
        self.playerLbl = Label(self, image=self.playerImg)
        self.playerLbl.place(x = self.x, y = self.y)

    #Check for collision
    def checkCollision(self):
        colX = range(self.bug.winfo_x() - 60, self.bug.winfo_x() + 60)
        colY = range(self.bug.winfo_y() - 96, self.bug.winfo_y() + 96)
        
        if (self.playerLbl.winfo_x() in colX) and (self.playerLbl.winfo_y() in colY):
            print("Hello ladybug!")

    #Player movement functions
    def moveLeft(self, event):
        self.playerLbl.place(x = self.playerLbl.winfo_x() - 10, y = self.playerLbl.winfo_y())
        self.checkCollision()

    def moveRight(self, event):
        self.playerLbl.place(x = self.playerLbl.winfo_x() + 10, y = self.playerLbl.winfo_y())
        self.checkCollision()

    def moveUp(self, event):
        self.playerLbl.place(x = self.playerLbl.winfo_x(), y = self.playerLbl.winfo_y() - 10)
        self.checkCollision()

    def moveDown(self, event):
        self.playerLbl.place(x = self.playerLbl.winfo_x(), y = self.playerLbl.winfo_y() + 10)
        self.checkCollision()

#Bug class
class Bug(Label):
    def __init__(self, master: Canvas, img: str, xRange: int, yRange: int):
        super().__init__(master=master)
        #Setup
        self.img = PhotoImage(file=img)
        self.config(image=self.img)

        self.randomPlace(xRange, yRange)

    #Random placement function
    def randomPlace(self, xRange: int, yRange: int):
        self.randX = random.randrange(0, xRange - 60)
        self.randY = random.randrange(0, yRange - (96 * 2))
        self.place(x = self.randX, y = self.randY)

#Main
if __name__ == "__main__":
    #Variables
    canvasWidth = 700
    canvasHeight = 500

    #Root Tk setup
    root = Tk()
    root.resizable(False, False)
    root.geometry(f"{canvasWidth}x{canvasHeight}")

    #Canvas
    canvas = MainCanvas(root, canvasWidth, canvasHeight)
    canvas.pack()

    #Binding buttons
    root.bind("<Left>", canvas.moveLeft)
    root.bind("<Right>", canvas.moveRight)
    root.bind("<Up>", canvas.moveUp)
    root.bind("<Down>", canvas.moveDown)

    root.mainloop()