from turtle import *
from random import randrange, sample
from _SETTINGS_ import init_X, init_Y, track_Width, turtle_Count, turtle_Colors, turtle_Shapes

def Add_Turtles(t):
    
    # Tạo thứ tự chạy ngẫu nhiên
    order = sample(range(0, turtle_Count), turtle_Count)
        
    for i in range(turtle_Count):
        position = (init_X, init_Y - track_Width*i - track_Width/2)
        color = turtle_Colors.pop(randrange(len(turtle_Colors)))
        shape = 'Characters/' + turtle_Shapes.pop(randrange(len(turtle_Shapes))) + '.gif'
        
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
        t[i][0].speed(5) # tăng tốc độ vào đường đua
        t[i][0].goto(0,-200)
        t[i][0].goto(t[i][2])
        t[i][0].speed(3) # tốc độ mặc định
        t[i][0].down()
        
    return t