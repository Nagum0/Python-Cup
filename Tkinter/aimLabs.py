from tkinter import *
import random

""" Target canvas """
class TargetCanvas(Canvas):
    def __init__(self, parent: Tk) -> None:
        super().__init__(master=parent, width=640, height=480, bg="green")
        self.pack()
        
        #Variables

        #Get mouse position
        self.bind_all("<Motion>", self.getMousePos)
        self.bind_all("<Button-1>", self.click)

    """ Get mouse x and y """
    def getMousePos(self, event) -> None:
        self.mouseX = event.x
        self.mouseY = event.y

    def click(self, event) -> None:
        print(self.mouseX, self.mouseY)

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