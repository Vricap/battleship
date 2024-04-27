from drawGrid import drawPlayerGrid

player1Grid = drawPlayerGrid()
player2Grid = drawPlayerGrid()
    
# print grid nicely
rowsCoordinate = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
}

def prGr(grid, r):
    x = 0
    for i in grid:
        print(r[x], i, "\n")
        x += 1
    
prGr(player1Grid, rowsCoordinate)
print("==================================================\n")
prGr(player2Grid, rowsCoordinate)

while True:
    row = input("Masukan row: ")
    coloumn = input("Masukan coloumn: ")

    player1Grid[int(row)][int(coloumn)] = "+"

    prGr(player1Grid, rowsCoordinate)
    print("==================================================\n")
    prGr(player2Grid, rowsCoordinate)