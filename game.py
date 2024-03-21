import pygame
import random
import sys
import asyncio

sys.setrecursionlimit(100000) # increase the limit recursion depth because i'm a terrible progammer

# create the ships
# ships spec:
    # carrier: 5
    # battleship: 4
    # destroyer: 3
    # submarine: 3
    # patrol boat: 2
ships = {
    "carrier": {
        "size": 5,
        "icon": "C"
    },
    "battleship": {
        "size": 4,
        "icon": "B"
    },
    "destroyer": {
        "size": 3,
        "icon": "D"
    },
    "submarine": {
        "size": 3,
        "icon": "S"
    },
    "patrol boat": {
        "size": 2,
        "icon": "P"
    }
}

# make a grid with 10x10 square 
def makeGrid():
    grid = []
    c = 1
    while c <= 10:
        c2 = 1
        iG = []
        while c2 <= 10:
            iG.append("-")
            c2 += 1
        grid.append(iG)
        c += 1
    return grid

# draw / place ship on grid randomly
def drawShip(makeGrid, size, icon):
    t = True
    while t:
        grid = makeGrid()
        p = random.randint(0, 1) # 0 for horizontal; 1 for vertical
        r = random.randint(0, 9) # row start position
        c = random.randint(0, 9) # coloumn start position
        
        if(p == 0):
            # TODO: REFACTOR: this code from here is similiar
            if(size + r >= 10 or size + c >= 10):
                continue
            c1 = c - 1
            for _ in range(size):
                c1 += 1
                if(grid[r][c1] != "-"):
                    drawShip(makeGrid, size, icon)
                grid[r][c1] = icon
            return grid

        elif(p == 1):
            if(size + r > 9 or size + c > 9):
                continue
            r1 = r - 1
            for _ in range(size):
                r1 += 1
                if(grid[r1][c] != "-"):
                    drawShip(makeGrid, size, icon)
                grid[r1][c] = icon
            return grid
        
def drawPlayerGrid():
    grid = []
    for ship in ships:
        grid.append(drawShip(makeGrid, ships[ship]["size"], ships[ship]["icon"]))
    
    # TODO: stupid temporary little fix. not good!
    counter = 0
    for i in grid:
        counter += i.count("-")
    while True:
        if(counter < 83):
            drawPlayerGrid()
        else:
            return grid

player1Grid = drawPlayerGrid()

# print grid nicely
def prGr(grid):
    for i in grid:
        print(i, "\n")
    
prGr(player1Grid)
# print("==================================================\n")
# prGr(player2Grid)

player1Shots = 20
player2Shots = 20

# while True:
