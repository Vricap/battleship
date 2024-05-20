from drawGrid import drawPlayerGrid

player1Grid = drawPlayerGrid()
player2Grid = drawPlayerGrid()
    
# rowsCoordinate = {
#     0: "A",
#     1: "B",
#     2: "C",
#     3: "D",
#     4: "E",
#     5: "F",
#     6: "G",
#     7: "H",
#     8: "I",
#     9: "J",
# }

def prGr(grid):
    x = 0
    for i in grid:
        print(i, "\n")
        x += 1

def isHit(row, coloumn, player):
    if(player == 1):
        if(player1Grid[int(row)][int(coloumn)] != "-"):
            if(player1Grid[int(row)][int(coloumn)] != "+"):
                return 1
    elif(player == 2):
        if(player2Grid[int(row)][int(coloumn)] != "-"):
            if(player2Grid[int(row)][int(coloumn)] != "+"):
                return 1
    return 0
    
prGr(player1Grid)
print("==================================================\n")
prGr(player2Grid)

player1Shot = 20
player2Shot = 20

winScore = 17

player1 = True
player2 = False

player1Score = 0
player2Score = 0

t = 40

while t > 0:
    if(player1Score == 17):
        print("PLAYER 1 WON")
        break
    elif(player2Score == 17):
        print("PLAYER 2 WON")
        break

    print("Shot player 1 left: ", player1Shot)
    print("Shot player 2 left: ", player2Shot)
    print("Player 1 score: ", player1Score)
    print("Player 2 score: ", player2Score)

    if(player1):
        print("Player 1 turn.")
    else:
        print("Player 2 turn.")

    row = input("Masukan row: ")
    coloumn = input("Masukan coloumn: ")


    if(player1):
        s = isHit(row, coloumn, 2)
        player1Score += s
        player2Grid[int(row)][int(coloumn)] = "+"
        player1 = False
        player2 = True
        player1Shot -= 1

    elif(player2):
        s = isHit(row, coloumn, 1)
        player2Score += s
        player1Grid[int(row)][int(coloumn)] = "+"
        player1 = True
        player2 = False
        player2Shot -= 1


    prGr(player1Grid)
    print("==================================================\n")
    prGr(player2Grid)
    t -= 1
    if(t == 0):
        print("DRAW!")