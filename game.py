import pygame
import random

# function to generate ship location 
def generatePos(ship):
    hori = 0
    vert = 1
    arr  = {
        "coor": [],
        "pos": ""
    }
    while True:
        pos = random.randint(0, 1)
        x = 0
        while x <= 9 and x >= 0:
            x = random.randint(0, 9)
            if(x + ship > 9):
                continue
            j = 1
            while j <= ship: 
                if(pos == vert):
                    arr["coor"].append(x + j)
                    arr["pos"] = "v"
                elif(pos == hori):
                    arr["coor"].append(x)
                    arr["pos"] = "h"
                j += 1
            break
        return arr

# create the ships
# ships spec:
    # carrier: 5
    # battleship: 4
    # destroyer: 3
    # submarine: 3
    # patrol boat: 2
ships = {
    "carrier": 5,
    "battleships": 4,
    "destroyer": 3,
    "submarine": 3,
    "patrol boat": 2
}

# generate ships location
location = {
    "carrier": generatePos(5),
    "battleships":generatePos(4),
    "destroyer": generatePos(3),
    "submarine": generatePos(3),
    "patrol boat": generatePos(2)
}

# print(location)

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

# place ships position in grid
def plcSh(grid, ship):
    gC = gC
    if(ship["pos"] == "h"):
        while True:
            n = random.randint(0, 9)
            for i in range(len(gC[n])):
                if(gC[n][i] == "*"):
                    gC = grid
                    break
                for j in ship["coor"]:
                    if(i == j):
                        gC[n][j] = "*"
            break
        grid = gC
            
plcSh(grid, {"coor": [2,3,4,5], "pos": "h"})
plcSh(grid, {"coor": [4,5,6], "pos": "h"})

def prGr(grid):
    for i in grid:
        print(i, "\n")
prGr(grid)
# # define background color
# background_color = (0,0,255)

# # define screen size
# screen = pygame.display.set_mode((1280, 700))

# # set the caption / title
# pygame.display.set_caption("Battleship AI")

# # fill the screen with bgc
# screen.fill(background_color)

# # update display using flip
# pygame.display.flip()

# # variable to keep game / window open / running
# running = True

# # loop game
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False