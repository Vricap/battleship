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
player1Grid = []
player2Grid = []
def makeGrid(grid):
    c = 1
    while c <= 10:
        c2 = 1
        iG = []
        while c2 <= 10:
            iG.append("-")
            c2 += 1
        grid.append(iG)
        c += 1
makeGrid(player1Grid)
makeGrid(player2Grid)
# print(grid)

# dr
# aw / place ship on grid randomly
def drawShip(grid, size, icon):
    cpG = list(grid)
    t = True
    while t:
        # p = random.randint(0, 1) # 0 for horizontal; 1 for vertical
        r = random.randint(0, 9) # row start position
        c = random.randint(0, 9) # coloumn start position

        p = 0
        # FIXME: there's some overlapping?? or out of place of the symbol placing
        if(p == 0):
            # TODO: REFACTOR: this code from here is similiar
            if(size + r >= 10 or size + c >= 10):
                continue
            c1 = c - 1
            for _ in range(size):
                c1 += 1
                if(cpG[r][c1] != "-"):
                    print(cpG, "\n")
                    cpG = list(grid)
                    print(cpG, "\n")
                    drawShip(cpG, size, icon)
                cpG[r][c1] = icon
            grid = list(cpG)
            return

        elif(p == 1):
            if(size + r > 9 or size + c > 9):
                continue
            r1 = r - 1
            for _ in range(size):
                r1 += 1
                if(cpG[r1][c] != "-"):
                    cpG = list(grid)
                    drawShip(cpG, size, icon)
                cpG[r1][c] = icon
            grid = list(cpG)
            return 
        
def drawPlayerGrid(grid):
    cpG = list(grid)
    for ship in ships:
        drawShip(cpG, ships[ship]["size"], ships[ship]["icon"])
    
    # TODO: stupid temporary little fix. not good!
    counter = 0
    for i in cpG:
        counter += i.count("-")
    while True:
        if(counter < 83):
            cpG = list(grid)
            drawShip(cpG, ships[ship]["size"], ships[ship]["icon"])
        else:
            print(counter)
            grid = list(cpG)
            return

drawPlayerGrid(player1Grid)
# drawPlayerGrid(player2Grid)

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
