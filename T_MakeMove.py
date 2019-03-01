from turtle import *
from random import randrange, choice
from time import perf_counter
from _SETTINGS_ import turtle_Back_Stop_Bias, turtle_Move_Length

def Make_Move(tx, trackLength_Session, race_Count):
    # Rùa đã về đích
    if (tx[9] == race_Count):
        pass
        
    else:

        # Rùa cán đích
        if (tx[9] % 2 == 0 and tx[0].distance(tx[2]) >= trackLength_Session) or (tx[9] % 2 == 1 and tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]) >= trackLength_Session):

            # Chặng cuối
            if (race_Count - tx[9] == 1):
                tx[8] = perf_counter() - tx[8]
                tx[0].clear()
                tx[9] += 1
                return tx

            # Không phải chặng cuối
            else:
                tx[0].left(180)
                tx[5] = 0
                tx[6] = 0
                tx[7] = 0
                tx[0].clear()
                tx[9] += 1
        
        # Rùa chưa cán đích
        x = choice(turtle_Move_Length)
        moveList = ['back', 'stop', 'fwd']
        move = choice(moveList)
        if move == 'back' and tx[5] % 10 >= turtle_Back_Stop_Bias and tx[5] % 10 <= 9 and tx[6] <= 3:
            tx[0].pencolor(bgcolor())
            tx[0].backward(x)
            tx[6] += 1
            tx[0].pencolor(tx[4])
        
        elif move == 'stop' and tx[5] % 10 >= turtle_Back_Stop_Bias and tx[5] % 10 <= 9 and tx[7] <= 2:
            tx[7] += 1
        
        elif move == 'fwd':
            if (tx[9] % 2 == 0 and tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]) <= x):
                tx[0].forward(tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]))
            elif (tx[9] % 2 == 1 and tx[0].distance(tx[2]) <= x):
                tx[0].forward(tx[0].distance(tx[2]))
            else:
                tx[0].forward(x)
        
        else:
            move = 'fwd'
            if (tx[9] % 2 == 0 and tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]) <= x):
                tx[0].forward(tx[0].distance(tx[2][0]+trackLength_Session, tx[2][1]))
            elif (tx[9] % 2 == 1 and tx[0].distance(tx[2]) <= x):
                tx[0].forward(tx[0].distance(tx[2]))
            else:
                tx[0].forward(x)
        
        tx[5] += 1
        
        # Reset bộ đếm nước đi sau mỗi 10 nước
        if (tx[5] // 10 > 0 and tx[5] % 10 == 0):
            tx[6] = 0
            tx[7] = 0
    
    # Kết thúc nước đi
    return tx
