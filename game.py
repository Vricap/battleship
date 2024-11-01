def isHit(grid, row, coloumn):
        if(grid[int(row)][int(coloumn)] != "-" and grid[int(row)][int(coloumn)] != "+"):
            # print("HIT!")
            return 1
        else:
            # print("MISS!")
            return 0

def playerCoordinatePicking():
    row = None
    coloumn = None
    t = True
    while t:
        # TODO: also check if input is a string
        print('Pick row from 0 to 9')
        row = int(input("Masukan row: "))
        if(row < 0 or row > 9):
            print('Your ROW is out of bound. Pick row from 0 to 9!')
            continue
        print('Pick coloumn from 0 to 9')
        coloumn = int(input("Masukan coloumn: "))
        if(coloumn < 0 or coloumn > 9):
            print('Your COLOUMN is out of bound. Pick coloumn from 0 to 9!')
            continue
                
        t = False
    return [row, coloumn]
        
if __name__ == "__main__":
    from drawGrid import drawPlayerGrid
    from gameAI import playAI
    from drawGrid import makeGrid

    player1Grid = drawPlayerGrid()
    player1TargetGrid = makeGrid()
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

    print('\n')
    print("YOUR SHIP GRID!")
    prGr(player1Grid)
    print("==================================================\n")
    print("YOUR TARGET MARK GRID!")
    prGr(player1TargetGrid)
    # prGr(player2Grid)

    player1Shot = 30
    player2Shot = 30

    winScore = 17

    player1 = True
    player2 = False

    player1Score = 0
    player2Score = 0

    t = 60

    row = None
    coloumn = None

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
        print("Player 2 score: ", player2Score, '\n')

        # if(player1):
        #     print("Player 1 turn.")
        # else:
        #     print("Player 2 turn.")


        if(player1):
            print("Player 1 turn.")
            if(t != 60 and s):
                print("Your last shot is HIT!")
            else:
                print("Your last shot is MISS!")
            print('Your last coordinate was: [', row, coloumn, ']\n')
            coordinate = playerCoordinatePicking()
            row = coordinate[0]
            coloumn = coordinate[1]
            s = isHit(player2Grid, row, coloumn)
            player1Score += s
            player2Grid[int(row)][int(coloumn)] = "+"
            player1TargetGrid[int(row)][int(coloumn)] = "+"
            player1 = False
            player2 = True
            player1Shot -= 1

        elif(player2):
            s2 = playAI(player1Grid)
            player2Score += s2
            player1 = True
            player2 = False
            player2Shot -= 1

        print('\n')
        print("YOUR SHIP GRID!")
        prGr(player1Grid)
        print("==================================================\n")
        print("YOUR TARGET MARK GRID!")
        prGr(player1TargetGrid)
        # prGr(player2Grid)
        t -= 1
        if(t == 0 and player1Score == player2Score):
            print("DRAW!")
        elif(t == 0 and player1Score > player2Score):
            print("PLAYER 1 WIN!")
        elif(t == 0 and player1Score < player2Score):
            print("PLAYER 2 WIN!")
