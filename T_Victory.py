from turtle import *
from _SETTINGS_ import rank_Width

def Animate_Winner(t, winner):
    t[winner][0].speed(1)
    t[winner][0].setheading(90) # hướng bắc trong standard mode
    t[winner][0].forward(rank_Width/4)
    while True:
        t[winner][0].forward(10)
        t[winner][0].backward(10)