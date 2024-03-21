import random

# def test(grid, ship):
#     while True:
#         n = random.randint(0,9)
#         if(ship["pos"] == "h"):
#             if("*" in ship["coor"][n]):
#                 continue
#             # TODO: code here
#         elif(ship["pos"] == 'v'):
#             r = True
#             for i in grid:
#                 if(i[ship["coor"][0]] == "*"):
#                     r = False
#                     break
#             # TODO: code here
#             if(r != True):
#                break

#     return

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

# test(grid, {"coor": [2,3,4,5], "pos": "h"})

def d(grid, ship):
    cpG = grid
    t = True
    while t:
        p = random.randint(0, 1) # 0 for horizontal; 1 for vertical
        r = random.randint(0, 8) # row start position
        c = random.randint(0, 9) # coloumn start position
        if(p == 0):
            # TODO:
            if(ship + r > 9 or ship + c > 9):
                continue
            for _ in range(ship):
                c += 1
                if(cpG[r][c] == "O"):
                    cpG = grid
                    return d(grid, ship)
                cpG[r][c] = "O"
            return

        elif(p == 1):
            # TODO:
            if(ship + r > 9 or ship + c > 9):
                continue
            for _ in range(ship):
                r += 1
                if(cpG[r][c] == "O"):
                    cpG = grid
                    return d(grid, ship)
                cpG[r][c] = "O"
            return

d(grid, 4)
d(grid, 3)
d(grid, 2)

def prGr(grid):
    for i in grid:
        print(i, "\n")
prGr(grid)