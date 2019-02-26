# HÀM MakeMove()

from turtle import *
from random import randrange, choice
from time import perf_counter

from _SETTINGS_ import turtleBackStopBias, turtleMoveLength, raceCount

def MakeMove(tx, trackLength_Session):
    if (tx[9] == raceCount):
        pass
    elif (tx[9] % 2 == 0 and tx[0].distance(tx[2]) >= trackLength_Session) or (tx[9] % 2 == 1 and tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]) >= trackLength_Session):
        if (raceCount - tx[9] == 1): tx[8] = perf_counter() - tx[8]
        tx[0].left(180)
        tx[5] = 0
        tx[6] = 0
        tx[7] = 0
        tx[0].clear()
        tx[9] += 1
    else:
        x = choice(turtleMoveLength)
        moveList = ['back', 'stop', 'fwd']
        move = choice(moveList)
        if move == 'back' and tx[5] % 10 >= turtleBackStopBias and tx[5] % 10 <= 9 and tx[6] <= 3:
            tx[0].pencolor(bgcolor())
            tx[0].backward(x)
            tx[6] += 1
            tx[0].pencolor(tx[4])
        elif move == 'stop' and tx[5] % 10 >= turtleBackStopBias and tx[5] % 10 <= 9 and tx[7] <= 2:
            tx[7] += 1
        elif move == 'fwd':
            tx[0].forward(x)
        else:
            move = 'fwd'
            tx[0].forward(x)
        tx[5] += 1
        if (tx[5] // 10 > 0 and tx[5] % 10 == 0):
            tx[6] = 0
            tx[7] = 0
    return tx
