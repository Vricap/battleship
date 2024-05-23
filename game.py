def isHit(grid, row, coloumn):
        if(grid[int(row)][int(coloumn)] != "-" and grid[int(row)][int(coloumn)] != "+"):
            return 1
        else:
            return 0
        
if __name__ == "__main__":
    from drawGrid import drawPlayerGrid
    from gameAI import playAI

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


        if(player1):
            # row = input("Masukan row: ")
            # coloumn = input("Masukan coloumn: ")
            row = 0
            coloumn = 0
            s = isHit(player2Grid, row, coloumn)
            player1Score += s
            player2Grid[int(row)][int(coloumn)] = "+"
            player1 = False
            player2 = True
            player1Shot -= 1

        elif(player2):
            s = playAI(player1Grid)
            player2Score += s
            player1 = True
            player2 = False
            player2Shot -= 1

        prGr(player1Grid)
        print("==================================================\n")
        prGr(player2Grid)
        t -= 1
        if(t == 0 and player1Score == player2Score):
            print("DRAW!")
        elif(t == 0 and player1Score > player2Score):
            print("PLAYER 1 WIN!")
        elif(t == 0 and player1Score < player2Score):
            print("PLAYER 2 WIN!")