# VẼ BẢNG XẾP HẠNG

from turtle import *

from _SETTINGS_ import initX, initY, trackCount, trackWidth, scoreboardPadding

def RankTurtles(t):
    rank = []
    
    initialList = []
    for i in range(len(t)): initialList.append(t[i][8])
    sortedList = sorted(initialList)
    
    for a in range(len(initialList)):
        for b in range(len(sortedList)):
            if initialList[a] == sortedList[b]:
                rank.append((b+1, round(initialList[a], 5)))
                break
            
    return rank

def DrawScoreboard(t):
    rankList = RankTurtles(t)
    columnWidth = 100
    speed(0.25)
    
    up()
    goto(initX - scoreboardPadding, initY + scoreboardPadding)
    down()
    
    d = [(-1,1), (1,-1), (-1,1), (1,1), (1,-1), (-1,1)]
    for i in range(len(d)):
        left(90*d[i][0])
        forward(2*scoreboardPadding + trackCount*trackWidth)
        left(90*d[i][1])
        forward(columnWidth)
    
    title = ['', 'RANK', 'TIME']
    up()
    right(90)
    forward(scoreboardPadding)
    right(90)
    mark = position()
    for i in range(3):
        forward(i*columnWidth + columnWidth/2)
        write(title[i], align='center', font='Consolas')
        goto(mark)
    
    goto(initX-20 + (3/2)*columnWidth, initY - 2/3*trackWidth)
    right(90)
    for i in range(trackCount):
        write(rankList[i][0], align='center', font='Consolas')
        left(90)
        forward(columnWidth)
        write(rankList[i][1], align='center', font='Consolas')
        backward(columnWidth)
        right(90)
        forward(trackWidth)
        