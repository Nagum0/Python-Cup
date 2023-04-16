from tkinter import *
import random

""" Funtcions """
def jump():
    global simonY
    global randY

    simonLbl.place(x=simonX, y=simonY)
    root.after(500, jump)

""" Variables """
root = Tk()
canvas = Canvas(root, width=640, height=480, bg="cyan")
randY = random.randint(100, 250)
print(randY)
direction = "up"

#Trampoline
trampolineImg = PhotoImage(file="Tkinter\\Files\\trampolina.png")
trampolineLbl = Label(canvas, image=trampolineImg, width=150, height=150, bg="cyan")

#Simon
simonImgList = ["p0", "p3"]
simonImg = PhotoImage(file=f"Tkinter\\Files\\Simon\\{simonImgList[0]}.png")
simonLbl = Label(canvas, image=simonImg, width=100, height=100, bg="cyan")
simonX = 270
simonY = 230

if __name__ == "__main__":
    """ Root tk setup """
    root.title("Trampoline")
    root.geometry("640x480")
    root.resizable(False, False)

    #Packing
    canvas.pack()
    trampolineLbl.place(x=245, y=300)
    simonLbl.place(x=simonX, y=simonY)

    #Functions
    jump()

    """ Mainloop """
    root.mainloop()