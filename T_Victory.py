from turtle import *
from _SETTINGS_ import rank_Width

def Animate_Winner(t, winner):
    t[winner][0].speed(1)
    t[winner][0].right(90)
    while True:
        t[winner][0].forward(rank_Width/8)
        t[winner][0].backward(rank_Width/8)