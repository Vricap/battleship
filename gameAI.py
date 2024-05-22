# How it work:
# First, will shot at random coordinate
# if hit, that coordinate will be the last hit coordinate
# and the next shot is around that coordinate (area) - y(1), y(-1), x(1), x(-1)
# if that shot is miss, the next shot is other possible coordinate. The last hit coordinate still the same
# if the shot is hit, that will be the current last hit coordinate. Thus, iterate the process again.

import random
from game import isHit

shotCor = []
lastHit = ""
searchMode = True
targerMode = False

def playAI(grid):
    if(searchMode):
        while True:
            x = random.randint(0, 9) # row 
            y = random.randint(0, 9) # coloumn 

            c = f"{x} {y}"
            if c in shotCor:
                continue
            
            shotCor.append(c)
            grid[x][y] = "+"
            s = isHit(grid, x, y)
            
            if(s == 1):
                lastHit = shotCor[-1]
                # searchMode = False
                # targerMode = True
                # return
            return grid

    # elif(targerMode):
        