from tkinter import *
import random

""" Target canvas """
class TargetCanvas(Canvas):
    def __init__(self, parent: Tk) -> None:
        super().__init__(master=parent, width=640, height=480, bg="green")
        self.pack()

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