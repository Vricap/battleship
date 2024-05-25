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
def drawShip(grid, size, icon, p):
    # TODO: REFACTOR: This is UGLY and STUPID
    cpG = list(grid)
    while True:        
        r = random.randint(0, 9) # row start position
        c = random.randint(0, 9) # coloumn start position

        # FIXME: there's some overlapping??
        if(p == 0):
            if(size + r > 9 or size + c > 9):
                continue
            c1 = c 
            t = []
            for _ in range(size):
                t = cpG[r][c1]
                c1 += 1

            # GOD.....
            if("S" in t or "P" in t or "B" in t or "D" in t or "C" in t):
                continue
            else:
                for _ in range(size):
                    cpG[r][c] = icon
                    c += 1
                grid = list(cpG)
                return

        elif(p == 1):
            if(size + r > 9 or size + c > 9):
                continue
            r1 = r 
            t = []
            for _ in range(size):
                t = cpG[r1][c]
                r1 += 1
            if("S" in t or "P" in t or "B" in t or "D" in t or "C" in t):
                continue
            else:
                for _ in range(size):
                    cpG[r][c] = icon
                    r += 1
                grid = list(cpG)
                return 
        
def drawPlayerGrid():
    while True:
        grid = makeGrid()
        for ship in ships:
            p = random.randint(0, 1) # 0 for horizontal; 1 for vertical
            drawShip(grid, ships[ship]["size"], ships[ship]["icon"], p)
        
        # TODO: stupid temporary little fix of the bug above.... fix the upstream bug!
        counter = 0
        for i in grid:
            counter += i.count("-")
        if(counter != 83):
            continue
        return grid