from tkinter import *
import random

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.resizable(False, False)

        #Pouch setup
        self.coin = PhotoImage(file="Tkinter\Files\minca.png")
        self.pouch = PhotoImage(file="Tkinter\Files\mesec.png")
        self.pouchLbl = Label(self, image=self.pouch, width=100, height=100)
        self.pouchLbl.place(x=240, y=400)

    def drawCoins(self, x: int, y: int):
        coinLbl = Label(self, image=self.coin)
        coinLbl.place(x=x, y=y)

if __name__ == "__main__":
    coinNum = int(input("Coins: "))
    root = Root()
    
    #Drawing coins
    for _ in range(coinNum):
        randX = random.randrange(30, 500)
        randY = random.randrange(30, 370)
        root.drawCoins(randX, randY)

    root.mainloop()