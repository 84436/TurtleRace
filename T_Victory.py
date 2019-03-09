from turtle import *
from _SETTINGS_ import rank_Width, YouWin

def Animate_Winner(t, winner):
    WinImage = Turtle()
    WinImage.hideturtle()
    addshape('Backgrounds/' + YouWin + '.gif')
    WinImage.shape('Backgrounds/' + YouWin + '.gif')
    WinImage.up()
    WinImage.goto(t[winner][0].position())
    WinImage.setheading(90)
    WinImage.forward(125)
    WinImage.showturtle()
    
    t[winner][0].speed(1)
    t[winner][0].setheading(90) # hướng bắc trong standard mode
    t[winner][0].forward(rank_Width/8)
    while True:
        t[winner][0].forward(10)
        t[winner][0].backward(10)