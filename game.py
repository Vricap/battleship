import pygame
import random

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
        "icon": "@"
    },
    "battleship": {
        "size": 4,
        "icon": "$"
    },
    "destroyer": {
        "size": 3,
        "icon": "^"
    },
    "submarine": {
        "size": 3,
        "icon": "&"
    },
    "patrol boat": {
        "size": 2,
        "icon": "%"
    }
}

# make a grid with 10x10 square 
grid = []
c = 1
while c <= 10:
    c2 = 1
    iG = []
    while c2 <= 10:
        iG.append("#")
        c2 += 1
    grid.append(iG)
    c += 1
# print(grid)

# draw / place ship on grid randomly
def drSh(grid, ship, icon):
    cpG = grid
    t = True
    while t:
        p = random.randint(0, 1) # 0 for horizontal; 1 for vertical
        r = random.randint(0, 9) # row start position
        c = random.randint(0, 9) # coloumn start position
        if(p == 0):
            # TODO:
            if(ship + r > 9 or ship + c > 9):
                continue
            for _ in range(ship):
                c += 1
                if(cpG[r][c] != "#"):
                    cpG = grid
                    return drSh(grid, ship, icon)
                cpG[r][c] = icon
            return

        elif(p == 1):
            # TODO:
            if(ship + r > 9 or ship + c > 9):
                continue
            for _ in range(ship):
                r += 1
                if(cpG[r][c] != "#"):
                    cpG = grid
                    return drSh(grid, ship, icon)
                cpG[r][c] = icon
            return
        
drSh(grid, ships["carrier"]["size"], ships["carrier"]["icon"])
drSh(grid, ships["battleship"]["size"], ships["battleship"]["icon"])
drSh(grid, ships["submarine"]["size"], ships["submarine"]["icon"])
drSh(grid, ships["destroyer"]["size"], ships["destroyer"]["icon"])
drSh(grid, ships["patrol boat"]["size"], ships["patrol boat"]["icon"])

# print grid nicely
def prGr(grid):
    for i in grid:
        print(i, "\n")
prGr(grid)
