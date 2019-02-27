from turtle import *
from _SETTINGS_ import turtleCount, rankInitX, rankInitY, rankWidth

def RankTurtles(t):
    rank = []
    
    initialList = []
    for i in range(len(t)): initialList.append(t[i][8])
    sortedList = sorted(initialList)
    
    for a in range(len(initialList)):
        for b in range(len(sortedList)):
            if initialList[a] == sortedList[b]:
                rank.append((b+1, round(initialList[a], 3)))
                break
            
    return rank

def DrawScoreboard(t):

    # Lấy ranklist
    rankList = RankTurtles(t)
    
    # Dọn dẹp và nhấc bút lên
    clear()
    for i in range(turtleCount):
        t[i][0].clear()
        t[i][0].up()
    
    # Vẽ nền bục
    goto(rankInitX, rankInitY)
    showturtle()
    down()
    forward(turtleCount * rankWidth)
    goto(rankInitX, rankInitY)
    left(90)
    
    # Vẽ từng bục
    mark = position()
    for i in range(turtleCount):
        forward((turtleCount - rankList[i][0] + 1) * rankWidth/2)
        right(90)
        forward(rankWidth)
        right(90)
        forward((turtleCount - rankList[i][0] + 1) * rankWidth/2)
        left(180)
    
    # Cho từng con rùa lên bục
    for i in range(turtleCount):
        t[i][0].goto(rankInitX + rankWidth/2 + rankWidth*i, rankInitY + (turtleCount - rankList[i][0] + 1)*(rankWidth/2) + rankWidth/4)
    
    # Ghi thời gian dưới bục
    up()
    goto(rankInitX, rankInitY)
    forward(rankWidth/8)
    right(90)
    forward(rankWidth/2)
    for i in range(turtleCount):
        if (i != 0): forward(rankWidth)
        write(rankList[i][1], align='center', font='Consolas')
        
    # Xong
    hideturtle()