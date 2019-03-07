from turtle import *
from winsound import *
from random import randrange
from time import perf_counter

from _SETTINGS_ import *
from T_DrawTracks import *
from T_AddTurtles import *
from T_MakeMove import *
from T_Scoreboard import *
from T_Victory import *

# Phiên bản
VERSION_STRING = 'TurtleRace revision 4'
print(VERSION_STRING)

# tk interface: vẽ menu .-.
from tkinter import *

# Menu chọn độ dài đường đua > Tạo biến global, đặt giá trị và destroy menu
def RTL_Menu_Set_Value(window, value):
    global l
    l = value
    window.destroy()

# Menu chọn độ dài đường đua
def RTL_Menu():
    root = Tk()
    root.title(VERSION_STRING)
    frame = Frame()
    textString = '-- Choose your racetrack length --'
    label1 = Label(frame, font='Consolas', height=2, text=textString)
    # Lambda vì widget Button() không return giá trị tới callback
    # http://effbot.org/zone/tkinter-callbacks.htm
    button1 = Button(frame, command=lambda: RTL_Menu_Set_Value(root, 1), text='Short\n(10 steps)', font='Consolas', fg='green', justify=CENTER, height=5, width=15)
    button2 = Button(frame, command=lambda: RTL_Menu_Set_Value(root, 2), text='Medium\n(20 steps)', font='Consolas', fg='blue', justify=CENTER, height=5, width=15)
    button3 = Button(frame, command=lambda: RTL_Menu_Set_Value(root, 3), text='Long\n(30 steps)', font='Consolas', fg='red', justify=CENTER, height=5, width=15)
    label1.pack(side=TOP)
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    frame.pack(padx=10, pady=10)
    root.mainloop()

# Menu chọn số lượt đua > Tạo biến global, đặt giá trị và destroy menu
def RC_Menu_Set_Value(window, value):
    global race_Count
    race_Count = value
    window.destroy()

# Menu chọn số lượt đua
def RC_Menu():
    root = Tk()
    root.title(VERSION_STRING)
    frame = Frame()
    textString = '-- Choose your race count --'
    label1 = Label(frame, font='Consolas', height=2, text=textString)
    # Lambda vì widget Button() không return giá trị tới callback
    # http://effbot.org/zone/tkinter-callbacks.htm
    button1 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 1), text='1', font='Consolas', justify=CENTER, height=2, width=5)
    button2 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 2), text='2', font='Consolas', justify=CENTER, height=2, width=5)
    button3 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 3), text='3', font='Consolas', justify=CENTER, height=2, width=5)
    button4 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 4), text='4', font='Consolas', justify=CENTER, height=2, width=5)
    button5 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 5), text='5', font='Consolas', justify=CENTER, height=2, width=5)
    button6 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 6), text='6', font='Consolas', justify=CENTER, height=2, width=5)
    button7 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 7), text='7', font='Consolas', justify=CENTER, height=2, width=5)
    button8 = Button(frame, command=lambda: RC_Menu_Set_Value(root, 8), text='8', font='Consolas', justify=CENTER, height=2, width=5)
    label1.pack(side=TOP)
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack(side=LEFT)
    button5.pack(side=LEFT)
    button6.pack(side=LEFT)
    button7.pack(side=LEFT)
    button8.pack(side=LEFT)
    frame.pack(padx=10, pady=10)
    root.mainloop()

# Tạo menu
RTL_Menu()
RC_Menu()

# Kiểm tra l với race_Count có tồn tại
try:
    l
    race_Count
except NameError:
    exit()
else:
    trackLength_Session = track_Unit_Count[l-1] * track_Unit_Length

# Phát nhạc nền
if (Audio_BGM != None):
    PlaySound('Audio/' + Audio_BGM + '.wav', SND_LOOP | SND_ASYNC)

# Đặt tốc độ vẽ
speed(0.5)

# Đổi tên cửa sổ turtle (canvas)
title(VERSION_STRING)

# Vẽ đường đua
if (BGP_file != None):
    bgpic('Backgrounds/' + BGP_file + '.gif')
    pencolor('white')
Draw_Tracks(track_Unit_Count[l-1])

# Tạo rùa và lấy thứ tự chạy
t = []
t = Add_Turtles(t)
order = []
for i in range(turtle_Count): order.append(t[i][1])

# Hàm kiểm tra tất cả con rùa đã hoàn thành cuộc đua chưa
def have_We_Won():
    sum = 0
    for i in range(turtle_Count): sum += t[i][9]
    if sum == turtle_Count * race_Count:
        return True
    else:
        return False

# Set timer cùng lúc
for i in range(turtle_Count): 
    t[i][8] = perf_counter()

# Bắt đầu đua
while have_We_Won() == False:
    for i in range(turtle_Count):
        t[order[i]] = Make_Move(t[order[i]], trackLength_Session, race_Count)
        # DEBUG
        # print(str(t[order[i]]) + ' ' + str(t[order[i]][0].distance(t[order[i]][2])))

# Dừng nhạc nền (để chuẩn bị cho hiệu ứng chiến thắng)
PlaySound(None, SND_ASYNC)

# Tìm rùa chiến thắng
winner = 0
minRuntime = t[0][8] # lấy đại con đầu tiên làm chuẩn
for i in range(turtle_Count):
    if t[i][8] < minRuntime:
        minRuntime = t[i][8]
        winner = i
print('%s has won the game.' % t[winner][3])

# Vẽ bảng xếp hạng
if (BGP_Win_file != None):
    bgpic('Backgrounds/' + BGP_Win_file + '.gif')
    pencolor('white')
Draw_Scoreboard(t)

# Chạy hiệu ứng chiến thắng
PlaySound('Audio/' + Audio_Win + '.wav', SND_ASYNC)
Animate_Winner(t, winner)

done()
