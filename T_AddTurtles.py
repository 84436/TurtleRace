from turtle import *
from random import randrange, sample
from _SETTINGS_ import initX, initY, trackWidth, turtleCount, turtleColors

def AddTurtles(t):
    r = sample(range(0, turtleCount), turtleCount)
    for i in range(4):
        t.append([Turtle(), r[i], (initX, initY - trackWidth*i - trackWidth/2), turtleColors.pop(randrange(len(turtleColors))), 0, 0, 0, False])
    return t