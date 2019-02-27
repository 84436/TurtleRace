from turtle import *
from _SETTINGS_ import initX, initY, trackCount, trackUnitLength, trackWidth, trackDivPadding

def DrawTracks(trackUnitCount_Session):

    # Vẽ vạch ngang
    up()
    goto(initX, initY)
    for i in range(trackCount + 1):
        mark = position()
        down()
        forward(trackUnitLength * trackUnitCount_Session);
        up()
        goto(mark)
        right(90)
        forward(trackWidth)
        left(90)
    
    # Vẽ vạch dọc
    up()
    goto(initX, initY)    
    for i1 in range(trackUnitCount_Session + 1):
        right(90)
        backward(trackDivPadding)
        write(i1, align='center')
        forward(trackDivPadding)
        mark = position()
        for i2 in range(trackCount):
            forward(trackDivPadding)
            down()
            forward(trackWidth - 2*trackDivPadding)
            up()
            forward(trackDivPadding)
        goto(mark)
        left(90)
        up()
        forward(trackUnitLength)
    
    # Lui ra khỏi tầm nhìn
    hideturtle()
