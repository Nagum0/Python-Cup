from turtle import *

def stvorec(d):
    for i in range(4):
        fd(d)
        rt(90)
        
def trojuh(strana):
    for i in range(3):
        fd(strana)
        lt(120)

def dom(velkost):
    stvorec(velkost)
    trojuh(velkost)

def domy9():
    for _ in range(9):
        dom(30)
        fd(30)

speed(3)
domy9()