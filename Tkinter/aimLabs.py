from tkinter import *
import random

""" Target canvas """
class TargetCanvas(Canvas):
    def __init__(self, parent: Tk) -> None:
        super().__init__(master=parent, width=640, height=480, bg="green")
        self.pack()
        
        #Variables
        self.parent = parent
        self.targetX1 = 250
        self.targetY1 = 250

        #Get mouse position
        self.bind_all("<Motion>", self.getMousePos)
        self.bind_all("<Button-1>", self.click)
        self.parent.after(800, self.genTarget)

    """ Gen target """
    def genTarget(self) -> None:
        self.target = self.create_rectangle(self.targetX1, self.targetY1, self.targetX1 + 50, self.targetY1 + 50, fill="red")

    """ Mouse functions """
    #Get mouse x and y
    def getMousePos(self, event) -> None:
        self.mouseX = event.x
        self.mouseY = event.y

    #Left click function
    def click(self, event) -> None:
        print(self.mouseX, self.mouseY)

        if self.checkHit() == True:
            print("Hit")
        else:
            print("Miss")

    """ Check for hit """
    def checkHit(self) -> bool:
        if self.mouseX > self.targetX1 and self.mouseX < self.targetX1+50 and self.mouseY > self.targetY1 and self.mouseY < self.targetY1+50:
            return True
        else:
            return False

""" Main driver """
if __name__ == "__main__":
    """ Root setup """
    root = Tk()
    root.title("Aim Labs")
    root.geometry("640x480")
    root.resizable(False, False)
    
    """ Init target canvas """
    canvas = TargetCanvas(root)
    """ Mainloop """
    root.mainloop()