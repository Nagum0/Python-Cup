from tkinter import *
import random

#Field class
class Field(Tk):
    def __init__(self):
        super().__init__()
        #Field setup
        self.resizable(False, False)
        self.fieldImg = PhotoImage(file="Tkinter\Files\ihrisko.png")
        self.fieldLbl = Label(self, image=self.fieldImg).pack()

#Ball class
class Ball(Label):
    def __init__(self, master: Tk):
        super().__init__(master)
        #Variables
        self.x = 95
        self.y = 165

        #Ball setup
        self.ball = PhotoImage(file="Tkinter\Files\lopta.png")
        self.configure(image=self.ball)
        self.place(x=self.x, y=self.y)

    #Kick function
    def kick(self, event):
        self.x = random.randrange(95, 465)
        self.y = random.randrange(0, 330)
        self.place(x=self.x, y=self.y)
        self.checkPos()

    def checkPos(self):
        #450 - 465; 140 - 190
        if (self.x >= 440 and self.x <= 465) and (self.y >= 130 and self.y <= 200):
            print("GOAL!")
        else:
            print("Missed!")

#Main
if __name__ == "__main__":
    #Field
    field = Field()
    #Ball
    ball = Ball(field)
    #Key binding
    field.bind("<space>", ball.kick)
    #Mainloop
    field.mainloop()