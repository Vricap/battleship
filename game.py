import pygame
import random

# function to generate ship location 
def generatePos(ship):
    hori = 0
    vert = 1
    posArr = []
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
                    posArr.append(x + j)
                elif(pos == hori):
                    posArr.append(x)
                j += 1
            break
        return posArr

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

print(location)

# make an 10x10 square
outerArr = []
c = 1
while c <= 10:
    c2 = 1
    innerArr = []
    while c2 <= 10:
        innerArr.append("#")
        c2 += 1
    outerArr.append(innerArr)
    c += 1


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