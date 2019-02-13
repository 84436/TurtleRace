# TURTLE RACE, the game

from turtle import *
from random import randrange
from os import system as s

from _SETTINGS_ import *
from T_BGM import *
from T_DrawTracks import *
from T_AddTurtles import *
from T_MakeMove import *

l = -1
while (l == -1):
    l = input('Chọn độ dài đường đua (1=short, 2=medium, 3=long): ')
    l = int(l)
    if (l-1 < 0) or (l-1 > 2):
        l = -1

PlayBGM()
trackLength_Session = trackUnitCount[l-1] * trackUnitLength
speed(0.125)
DrawTracks(trackUnitCount[l-1])

t = []
t = AddTurtles(t)
order = []
for i in range(turtleCount): order.append(t[i][1])


print(order)

for i in range(turtleCount):
    t[order[i]][0].color(t[order[i]][3])
    t[order[i]][0].up()
    t[order[i]][0].goto(t[order[i]][2])
    t[order[i]][0].down()
    #s("PAUSE > NUL")

def haveWeWon():
    sum = 0;
    for i in range(turtleCount): sum += t[i][7]
    if sum == turtleCount:
        return True
    else:
        return False

while haveWeWon() == False:
    for i in range(turtleCount):
        t[order[i]] = MakeMove(t[order[i]], trackLength_Session)
        
for i in range(turtleCount): print(t[i])

#winner = 0
#minMoves = tm[0][3] # lấy đại con đầu tiên làm chuẩn so sánh :v
#for i in range(turtleCount):
#    print('#%d: finished after %d moves' % (i, tm[i][3]))
#    if tm[i][3] < minMoves:
#        minMoves = tm[i][3]
#        winner = i
#print('Turtle #%d has won the game. Yay.' % winner)

s("PAUSE")
bye()

#t = []
#
#for i in range(turtleCount):
#    t.append(Turtle())
#    t[i].up()
#    t[i].goto(-200,-50*i)
#    t[i].down()
#    tm.append([False, t[i].position(), turtleColor_Session.pop(randrange(len(turtleColor_Session))), 0, 0, 0])
#    t[i].color(tm[i][2])
#
#
#print()
#for i in range(turtleCount):
#    print('#%d/states: %s' % (i, str(tm[i])))
#    print('#%d/distance from origin: %d' % (i, t[i].distance(tm[i][1])))
#    print()
#
#s("PAUSE")
#bye()