from turtle import *
from _SETTINGS_ import turtle_Count, rank_Init_X, rank_Init_Y, rank_Width

def Rank_Turtles(t):
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

def Draw_Scoreboard(t):

    # Lấy ranklist
    rankList = Rank_Turtles(t)
    
    # Dọn dẹp và nhấc bút lên
    clear()
    for i in range(turtle_Count):
        t[i][0].clear()
        t[i][0].up()
    
    # Vẽ nền bục
    goto(rank_Init_X, rank_Init_Y)
    showturtle()
    down()
    forward(turtle_Count * rank_Width)
    goto(rank_Init_X, rank_Init_Y)
    left(90)
    
    # Vẽ từng bục
    mark = position()
    for i in range(turtle_Count):
        forward((turtle_Count - rankList[i][0] + 1) * rank_Width/2)
        right(90)
        forward(rank_Width)
        right(90)
        forward((turtle_Count - rankList[i][0] + 1) * rank_Width/2)
        left(180)
    
    # Cho từng con rùa lên bục
    for i in range(turtle_Count):
        t[i][0].goto(rank_Init_X + rank_Width/2 + rank_Width*i, rank_Init_Y + (turtle_Count - rankList[i][0] + 1)*(rank_Width/2) + rank_Width/4)
    
    # Ghi thời gian dưới bục
    up()
    goto(rank_Init_X, rank_Init_Y)
    forward(rank_Width/8)
    right(90)
    forward(rank_Width/2)
    for i in range(turtle_Count):
        if (i != 0): forward(rank_Width)
        write(rankList[i][1], align='center', font='Consolas')
        
    # Xong
    hideturtle()