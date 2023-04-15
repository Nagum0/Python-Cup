from tkinter import *
import time
import random

def hideNum(txt: StringVar, randNum: int):
    txt.set("")

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400")
    root.resizable(False, False)

    #Label
    randNum = random.randrange(1000, 10000)
    numStr = StringVar()
    numStr.set(randNum)
    numLbl = Label(root, textvariable = numStr, font = ("Calibri", 50)).pack(pady=100)

    while True:
        root.update()
        time.sleep(1)
        hideNum(numStr, randNum)

        guess = str(input("What was the number? "))

        if guess == str(randNum):
            numStr.set("SUPER")
        else:
            numStr.set(randNum)
            print("WRONG")