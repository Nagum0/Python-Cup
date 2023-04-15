import tkinter as tk

#Main class
class MyCanvas(tk.Canvas):
    def __init__(self, master,x: int, y: int, sWidth: int, sHeight: int):
        super().__init__(master, width=800, height=600) 
        self.counter = 0
        self.moveX = 5
        self.x = x
        self.y = y
        self.sWidth = sWidth
        self.sHeight = sHeight

        self.sq = self.create_rectangle(self.x, self.y, self.x + self.sWidth, self.y + self.sHeight, fill="green", outline="green", tags="sq")

    def moveSquare(self):
        self.counter += self.moveX

        if self.counter <= 0:
            self.moveX = 5
        if self.counter >= 750:
            self.moveX = -5

        self.move(self.sq, self.moveX, 0)

#Main
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    
    #Canvas
    canvas = MyCanvas(root, 0, 130, 50, 50)
    canvas.pack(pady=125)

    #Mainloop
    while True:
        root.update()
        root.after(10, canvas.moveSquare())

    root.mainloop()
