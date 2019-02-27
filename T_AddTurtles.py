from turtle import *
from random import randrange, sample
from _SETTINGS_ import initX, initY, trackWidth, turtleCount, turtleColors, turtleShapes

def AddTurtles(t):
    
    # Tạo thứ tự chạy ngẫu nhiên
    order = sample(range(0, turtleCount), turtleCount)
        
    for i in range(turtleCount):
        position = (initX, initY - trackWidth*i - trackWidth/2)
        color = turtleColors.pop(randrange(len(turtleColors)))
        shape = 'Characters/' + turtleShapes.pop(randrange(len(turtleShapes))) + '.gif'
        
        # Thứ tự:
        # Turtle(), order, position, shape, color, moveCount, backCount, stopCount, runtime, raceCount
        t.append([Turtle(), order[i], position, shape, color, 0, 0, 0, 0.0, 0])
        
        # Apply hình dạng, màu nét vẽ
        t[i][0].hideturtle()
        t[i][0].color(color)
        addshape(shape)
        t[i][0].shape(shape)
        t[i][0].up()
        t[i][0].goto(0, -300)
        
        # Đưa rùa vào vị trí xuất phát
        t[i][0].showturtle()
        t[i][0].goto(0,-200)
        t[i][0].goto(t[i][2])
        t[i][0].down()
        
    return t