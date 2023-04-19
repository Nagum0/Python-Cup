from tkinter import *
import random

class MainCanvas(Canvas):
    def __init__(self, parent: Tk):
        super().__init__(master=parent, width=640, height=480)
        self.pack()

        """ Footprint """
        self.footPrintList = [0, 1, 2, 3, 4]
        self.randIndex = random.randint(0, len(self.footPrintList) - 1)
        self.stopy0 = Animal(self, f"ULOHA\Files\stopy{self.footPrintList[self.randIndex]}.png", 50, 350, self.randIndex)

        """ Animals """
        self.zviera0 = Animal(self, "ULOHA\Files\zviera0.png", 50, 50, 0)
        self.zviera01 = Animal(self, "ULOHA\Files\zviera1.png", 160, 100, 1)
        self.zviera02 = Animal(self, "ULOHA\Files\zviera2.png", 250, 40, 2)
        self.zviera03 = Animal(self, "ULOHA\Files\zviera3.png", 350, 100, 3)
        self.zviera04 = Animal(self, "ULOHA\Files\zviera4.png", 400, 30, 4)

""" Animal class """
class Animal(Label):
    def __init__(self, parent: Canvas, img: str, x: int, y: int, tag: int):
        super().__init__(master=parent)
        self.img = img
        self.tag = tag
        self.x = x
        self.y = y
        self.parent = parent

        self.mainImg = PhotoImage(file=self.img)
        self.config(image=self.mainImg)
        self.place(x=self.x, y=self.y)

        self.bind("<Button-1>", self.click)

    def click(self, event):
        self.y = 300
        self.place(x=self.x, y=self.y)
        self.move()

    def move(self):
        self.x += 50
        self.place(x = self.x, y=self.y)
        self.parent.after(400, self.move)

        if self.x >= 680:
            quit()

if __name__ == "__main__":
    root = Tk()
    root.geometry("640x480")
    root.resizable(False, False)

    root.update()
    canvas = MainCanvas(root)

    root.mainloop()