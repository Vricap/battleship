# How it work:
# First, will shot at random coordinate
# if hit, that coordinate will be the last hit coordinate
# and the next shot is around that coordinate (area) - y(1), y(-1), x(1), x(-1)
# if that shot is miss, the next shot is other possible coordinate. The last hit coordinate still the same
# if the shot is hit, that will be the current last hit coordinate. Thus, iterate the process again.

import random

shotCor = []

def gameAI(grid):
    x = random.randint(0, 9) # row 
    y = random.randint(0, 9) # coloumn 
    
    return