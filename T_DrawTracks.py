from turtle import *
from _SETTINGS_ import init_X, init_Y, turtle_Count, track_Unit_Length, track_Width, track_Div_Padding, track_Padding

def Draw_Tracks(trackUnitCount_Session):

    #     090
    # 180     000
    #     270

    # Vẽ vạch ngang
    up()
    setheading(0)
    goto(init_X, init_Y)
    for i in range(turtle_Count + 1):
        mark = position()
        down()
        forward(track_Unit_Length * trackUnitCount_Session);
        up()
        goto(mark)
        setheading(270)
        forward(track_Width)
        setheading(0)
    
    goto(init_X, init_Y)
    setheading(270)
    down()
    forward(turtle_Count * track_Width)
    up()
    goto(init_X + track_Unit_Length * trackUnitCount_Session, init_Y)
    down()
    forward(turtle_Count * track_Width)
    up()
    
    # Vẽ vạch dọc
    if (track_Padding == True):
        goto(init_X + track_Unit_Length, init_Y)    
        for i1 in range(trackUnitCount_Session - 1):
            setheading(270)
            mark = position()
            for i2 in range(turtle_Count):
                forward(track_Div_Padding)
                down()
                forward(track_Width - 2*track_Div_Padding)
                up()
                forward(track_Div_Padding)
            goto(mark)
            setheading(0)
            up()
            forward(track_Unit_Length)
    else:
        setheading(0)
    
    # Lui ra khỏi tầm nhìn
    hideturtle()
