# TURTLE RACE, the game

from turtle import *
from random import randrange
from time import perf_counter

from _SETTINGS_ import *
from T_BGM import *
from T_DrawTracks import *
from T_AddTurtles import *
from T_MakeMove import *
from T_Scoreboard import *

# Chọn độ dài
l = -1
while (l == -1):
    l = input('Choose racetrack length (1=short, 2=medium, 3=long): ')
    l = int(l)
    if (l-1 < 0) or (l-1 > 2): l = -1
trackLength_Session = trackUnitCount[l-1] * trackUnitLength

# Phát nhạc nền
PlayBGM()

# Vẽ đường đua
speed(0.125)
DrawTracks(trackUnitCount[l-1])

# Tạo rùa và lấy thứ tự chạy
t = []
t = AddTurtles(t)
order = []
for i in range(turtleCount): order.append(t[i][1])

# Đưa rùa vào vị trí xuất phát
for i in range(turtleCount):
    t[order[i]][0].up()
    t[order[i]][0].goto(t[order[i]][2])
    t[order[i]][0].down()

# Hàm kiểm tra tất cả con rùa đã hoàn thành cuộc đua chưa
def haveWeWon():
    sum = 0;
    for i in range(turtleCount): sum += t[i][9]
    if sum == turtleCount:
        return True
    else:
        return False

# Set timer cùng lúc
for i in range(turtleCount): t[order[i]][8] = perf_counter()

# Bắt đầu đua
while haveWeWon() == False:
    for i in range(turtleCount):
        t[order[i]] = MakeMove(t[order[i]], trackLength_Session)
        
# Debug: hiện trạng thái của rùa sau khi kết thúc cuộc đua
for i in range(turtleCount): print(t[i])

# Tìm rùa chiến thắng
winner = 0
minRuntime = t[0][8] # lấy đại con đầu tiên làm chuẩn
for i in range(turtleCount):
    if t[i][8] < minRuntime:
        minRuntime = t[i][8]
        winner = i
print('%s has won the game.' % t[winner][3])

# Vẽ bảng điểm
for i in range(turtleCount):
    t[i][0].clear()
clear()
for i in range(turtleCount):
    t[i][0].up()
    t[i][0].goto(t[i][2])
    t[i][0].forward(2*trackDivPadding)
DrawScoreboard(t)

done()
