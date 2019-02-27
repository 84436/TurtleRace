from turtle import *

def AnimateWinner(t, winner):
    t[winner][0].speed(1)
    t[winner][0].right(90)
    while True:
        t[winner][0].forward(20)
        t[winner][0].backward(20)