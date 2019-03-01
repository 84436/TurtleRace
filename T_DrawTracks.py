from turtle import *
from _SETTINGS_ import init_X, init_Y, turtle_Count, track_Unit_Length, track_Width, track_Div_Padding

def Draw_Tracks(trackUnitCount_Session):

    # Vẽ vạch ngang
    up()
    goto(init_X, init_Y)
    for i in range(turtle_Count + 1):
        mark = position()
        down()
        forward(track_Unit_Length * trackUnitCount_Session);
        up()
        goto(mark)
        right(90)
        forward(track_Width)
        left(90)
    
    # Vẽ vạch dọc
    up()
    goto(init_X, init_Y)    
    for i1 in range(trackUnitCount_Session + 1):
        right(90)
        # Ý nghĩa?
        # backward(track_Div_Padding)
        # write(i1, align='center')
        # forward(track_Div_Padding)
        mark = position()
        for i2 in range(turtle_Count):
            forward(track_Div_Padding)
            down()
            forward(track_Width - 2*track_Div_Padding)
            up()
            forward(track_Div_Padding)
        goto(mark)
        left(90)
        up()
        forward(track_Unit_Length)
    
    # Lui ra khỏi tầm nhìn
    hideturtle()
