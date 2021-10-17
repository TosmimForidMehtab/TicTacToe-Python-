# Creating a board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None
gameNotOver = True
currentPlayer = "X"


def displayBoard():
    # for i in range(10):
    #     print("", "_", end="")
    # print()
    print(" | ", board[0], " | ", board[1], " | ", board[2], " | ")
    print(" | ", board[3], " | ", board[4], " | ", board[5], " | ")
    print(" | ", board[6], " | ", board[7], " | ", board[8], " | ")


def playerTurns(player):
    print("For ", player)
    position = input("Enter position: ")
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter position from 1 to 9: ")
        position = int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("Position already acquired. Enter again")
    board[position] = player
    displayBoard()


def checkRows():
    global gameNotOver
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameNotOver = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def checkColumns():
    global gameNotOver
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameNotOver = False
    if col1:
        return board[0]
    if col2:
        return board[1]
    if col3:
        return board[2]
    return


def checkDiagonal():
    global gameNotOver
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        gameNotOver = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return


def checkWin():
    global winner
    rowWinner = checkRows()

    columnWinner = checkColumns()

    diagonalWinner = checkDiagonal()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return


def checkTie():
    global gameNotOver
    if "-" not in board:
        gameNotOver = False
    return


def checkGameOver():
    checkTie()
    checkWin()


def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return


def playGame():
    displayBoard()
    global gameNotOver
    global currentPlayer
    global winner
    while gameNotOver:
        playerTurns(currentPlayer)

        checkGameOver()

        flipPlayer()

    if winner == "X" or winner == "O":
        print(winner, " WON")
        return
    elif winner == None:
        print("TIE")
        return


playGame()
