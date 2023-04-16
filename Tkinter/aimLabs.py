from tkinter import *
import random

""" Target canvas """
class TargetCanvas(Canvas):
    def __init__(self, parent: Tk) -> None:
        super().__init__(master=parent, width=640, height=480, bg="green")
        self.pack()
        
        #Variables
        self.parent = parent
        self.score = 0

        #Get mouse position
        self.bind_all("<Motion>", self.getMousePos)
        self.bind_all("<Button-1>", self.click)

    """ Gen target """
    def genTarget(self) -> None:
        self.targetX1 = random.randint(100, 540)
        self.targetY1 = random.randint(50, 350)

        self.target = self.create_rectangle(self.targetX1, self.targetY1, self.targetX1 + 50, self.targetY1 + 50, fill="red", tags="target")

        self.parent.after(800, self.genTarget)

    """ Del target """
    def delTarget(self) -> None:
        self.parent.after(800, self.delete(self.target))

    """ Mouse functions """
    #Get mouse x and y
    def getMousePos(self, event) -> None:
        self.mouseX = event.x
        self.mouseY = event.y

    #Left click function
    def click(self, event) -> None:
        if self.checkHit() == True:
            self.score += 1
            print("Hit")
        else:
            self.score -= 2
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
    canvas.genTarget()
    canvas.delTarget()

    """ Mainloop """
    root.mainloop()