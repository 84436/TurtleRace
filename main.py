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

# Kiểm tra số rùa trong _SETTINGS_
if turtle_Count <= 0:
    print('Invalid number of turtles.')
    exit()

# Chọn độ dài
l = 0
while (l == 0):
    l = input('Choose racetrack length (1=short, 2=medium, 3=long): ')
    try:
        l = int(l)
        if (l < 1) or (l > 3):
            print('Invalid choice')
            l = 0
    except ValueError:
        print('Invalid number')
        l = 0
trackLength_Session = track_Unit_Count[l-1] * track_Unit_Length

# Số lượt đua
race_Count = 0
while (race_Count == 0):
    race_Count = input('Enter number of races: ')
    try:
        race_Count = int(race_Count)
        if (race_Count <= 0):
            print('Number out of range')
            race_Count = 0
    except ValueError:
        print('Invalid number')
        race_Count = 0

# Phát nhạc nền
if (Audio_BGM != None):
    PlaySound('Audio/' + Audio_BGM + '.wav', SND_LOOP | SND_ASYNC)

# Vẽ đường đua
if (BGP_file != None):
    bgpic('Backgrounds/' + BGP_file + '.gif')
    pencolor('white')
speed(0.5)
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
