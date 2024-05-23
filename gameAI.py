# How it work:
# First, will shot at random coordinate
# if hit, that coordinate will be the last hit coordinate
# and the next shot is around that coordinate (area) - y(1), y(-1), x(1), x(-1) randomly
# if that shot is miss, the next shot is other possible coordinate. The last hit coordinate still the same
# if the shot is hit, that will be the current last hit coordinate. Thus, iterate the process again.

import random
from game import isHit

searchCor = []
targetCor = []
targetInd = []
lastHit = 0
searchMode = True
targetMode = False

def playAI(grid):
    global searchCor
    global targetCor
    global targetInd
    global lastHit
    global searchMode
    global targetMode

    if(searchMode):
        while True:
            x = random.randint(0, 9) # row 
            y = random.randint(0, 9) # coloumn 

            c = f"{x} {y}"
            if c in searchCor: # skip if the coordinate have been shot
                continue
            
            searchCor.append(c) # record the coordinate
            s = isHit(grid, x, y) # check if hit
            grid[x][y] = "+" # paint the grid
            
            if(s == 1):
                lastHit = searchCor[-1].split()
                lastHit = [int(v) for v in lastHit]
                searchMode = False
                targetMode = True
            return s

    elif(targetMode):
        targetCor = [[lastHit[0], lastHit[1] + 1], [lastHit[0], lastHit[1] - 1], [lastHit[0] + 1, lastHit[1]], [lastHit[0] - 1, lastHit[1]]]

        while True:
            r = random.randint(0, len(targetCor) - 1)
            if(r in targetInd):
                continue
            targetInd.append(r)

            if len(targetInd) >= 4:
                targetInd = []
                targetMode = False
                searchMode = True
                return playAI(grid)

            # check if out of bound
            n = any(number > 18 for number in targetCor[r])
            if n:
                continue
            n = any(number < 0 for number in targetCor[r])
            if n:
                continue

            if(grid[targetCor[r][0]][targetCor[r][1]] == "+"): # check if already been shot
                continue
            
            s = isHit(grid, targetCor[r][0], targetCor[r][1]) # check if hit
            grid[targetCor[r][0]][targetCor[r][1]] = "+" # paint the grid
            if(s == 1):
                lastHit = [targetCor[r][0], targetCor[r][1]]
                targetInd = []
            return s