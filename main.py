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

# Chọn độ dài
l = -1
while (l == -1):
    l = input('Choose racetrack length (1=short, 2=medium, 3=long): ')
    l = int(l)
    if (l-1 < 0) or (l-1 > 2): l = -1
trackLength_Session = trackUnitCount[l-1] * trackUnitLength

# Phát nhạc nền
if (Audio_BGM != None):
    PlaySound('Audio/' + Audio_BGM + '.wav', SND_LOOP | SND_ASYNC)

# Vẽ đường đua
if (BGPfile != None):
    bgpic('Backgrounds/' + BGPfile + '.gif')
    pencolor('white')
speed(0.5)
DrawTracks(trackUnitCount[l-1])

# Tạo rùa và lấy thứ tự chạy
t = []
t = AddTurtles(t)
order = []
for i in range(turtleCount): order.append(t[i][1])

# Hàm kiểm tra tất cả con rùa đã hoàn thành cuộc đua chưa
def haveWeWon():
    sum = 0;
    for i in range(turtleCount): sum += t[i][9]
    if sum == turtleCount*raceCount:
        return True
    else:
        return False

# Set timer cùng lúc
for i in range(turtleCount): 
    t[i][8] = perf_counter()

# Bắt đầu đua
while haveWeWon() == False:
    for i in range(turtleCount):
        t[order[i]] = MakeMove(t[order[i]], trackLength_Session)
        # DEBUG
        # print(str(t[order[i]]) + ' ' + str(t[order[i]][0].distance(t[order[i]][2])))

# Dừng nhạc nền (để chuẩn bị cho hiệu ứng chiến thắng)
PlaySound(None, SND_ASYNC)

# Tìm rùa chiến thắng
winner = 0
minRuntime = t[0][8] # lấy đại con đầu tiên làm chuẩn
for i in range(turtleCount):
    if t[i][8] < minRuntime:
        minRuntime = t[i][8]
        winner = i
print('%s has won the game.' % t[winner][3])

# Vẽ bảng xếp hạng
DrawScoreboard(t)

# Chạy hiệu ứng chiến thắng
PlaySound('Audio/' + Audio_Win + '.wav', SND_ASYNC)
AnimateWinner(t, winner)

done()
