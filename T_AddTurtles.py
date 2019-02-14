# TẠO RÙA

from turtle import *
from random import randrange, sample

from _SETTINGS_ import initX, initY, trackWidth, turtleCount, turtleColors, turtleShapes

def AddTurtles(t):
    
    order = sample(range(0, turtleCount), turtleCount)
    moveCount = 0
    backCount = 0
    stopCount = 0
    win = False
    runtime = 0.0
    
    for i in range(turtleCount):
        position = (initX, initY - trackWidth*i - trackWidth/2)
        color = turtleColors.pop(randrange(len(turtleColors)))
        shape = 'Resources/' + turtleShapes.pop(randrange(len(turtleShapes))) + '.gif'
        
        t.append([Turtle(), order[i], position, shape, color, moveCount, backCount, stopCount, runtime, win])
        
        t[i][0].hideturtle()
        t[i][0].up()
        t[i][0].goto(0, 200)
        t[i][0].down()
        t[i][0].color(color)
        addshape(shape)
        t[i][0].shape(shape)
        t[i][0].showturtle()
        
    return t