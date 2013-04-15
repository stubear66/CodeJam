
def check_win(L):
    """ L is a list which contains either a row, column or diagonal """
    valid = "XOT."
    counts = {}
    print L
    for c in valid:
        counts[c] = 0
    for i in L:
        counts[i] += 1
    if counts["."] > 0:
        return ""
    for i in L:  
        if (counts[i] == 3 and counts['T'] == 1) or counts[i] == 4:
            return i + " won"
    
    return ""

def evaluate_board(board):
    """ board is a 4 x 4 2d array that contain either X O or .
    """
    column = []
    for i in board: #check horizontal
        #print i
        status = check_win(i)
        if status != "":
            return status
    # check vertical
    for col in range(len(board)):
        #print "Checking column : " + str(col)
        for row in range(len(board)):
            column.append(board[row][col])
        # print column
        status = check_win(column)
        if status != "":
            return status

    #check diagonal
    # only valid diagonals are [0,0][1,1][2,2][3,3]
    # and [0,3][1,2][2,1][3,0]
    diag1 = []
    diag2 = []
    for row in range(len(board)):
        diag1.append(board[row][row])
        diag2.append(board[3-row][row])
    status = check_win(diag1)
    if status != "":
        return status
    status = check_win(diag2)
    if status != "":
        return status

    # No winner so is it a draw or not completed?
    if board.count(".") == 0:
        return "Draw"
            
    return "Game has not completed"    
    # Ways to win
    # Horizontally  - TXXX XTXX XXTX XXXT XXXX
    # Vertically  [1]
    # Diagonally
    
    


f = open("A-small-attempt0.in.txt", "r")
numTest=f.readline()
#print numTest
case = 1
w, h = 4, 4
board = [[None] * w for i in range(h)]
lineNum = 0
for line in f:
    line = line.rstrip()
    letters = []
    #print line
    letters = [ c for c in line ]
    for j in range(len(letters)):
        board[lineNum][j] = letters[j]
    lineNum += 1

    if len(line) == 0:
        lineNum = 0
        r = evaluate_board(board)
        print "Case #" + str(case) + ": " + r
        board = [[None] * w for i in range(h)]
        case +=1
        
        

        


        
    
   
        
    
