"""Given two cells on the standard chess board, determine whether they
have the same color or not.

Example-
For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true 
For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false"""

def chessBoardCellColor(cell1, cell2):
    
    def getX(pos):
        return ord(pos[0]) - ord('A')
    def getY(pos):
        return ord(pos[0]) - ord('1')

    sum1 = getX(cell1[0]) + getY(cell1[1])
    sum2 = getX(cell2[0]) + getY(cell2[1])
    if sum1 % 2 == sum2 % 2:
        return True
    return False
