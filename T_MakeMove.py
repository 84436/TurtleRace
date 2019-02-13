#!/usr/bin/env python
# HÀM MakeMove()

# Thư viện
from turtle import *
from random import randrange, choice
from time import sleep

# Tệp settings: trackLength, moveLength
from _SETTINGS_ import turtleBackStopBias, turtleMoveLength

# tm (turtle metadata):
# 0:hasWon, 1:initPos, 2:penColor, 3:moveCount, 4:backCount, 5:stopCount

def MakeMove(tx, trackLength_Session):
    if tx[0].distance(tx[2]) >= trackLength_Session:
        tx[7] = True
    else:
        x = choice(turtleMoveLength)
        moveList = ['back', 'stop', 'fwd']
        move = choice(moveList)
        if move == 'back' and tx[4] % 10 >= turtleBackStopBias and tx[4] % 10 <= 9 and tx[5] <= 3:
            tx[0].pencolor(bgcolor())
            tx[0].backward(x)
            tx[5] += 1
            tx[0].pencolor(tx[3])
        elif move == 'stop' and tx[4] % 10 >= turtleBackStopBias and tx[4] % 10 <= 9 and tx[6] <= 2:
            tx[6] += 1
        
        elif move == 'fwd':
            tx[0].forward(x)
        else:
            move = 'fwd'
            tx[0].forward(x)
        
        tx[4] += 1
        
        # print("%d; %d; %d; %s" % (tx[4], x, tx[0].distance(tm[1]), move))
        
        if (tx[4] // 10 > 0 and tx[4] % 10 == 0):
            tx[5] = 0
            tx[6] = 0
            # print()
        
        # sleep(50/1000)
        
    return tx

##################################################
