#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
def signOnRow(grid, rowIndex, sign):
    for row in range(len(grid[rowIndex])):
        if sign != grid[row][rowIndex]:
            return False       
    return True  # TO CHANGE !!
  

#   @param grid   (an array 2D)
#   @param columnIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
def signOnColumn(grid, columnIndex, sign):
    for col in range(len(grid[columnIndex])):
        if sign != grid[columnIndex][col]:
            return False
    return True
        
    # TODO !!


#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if a DIAGONAL is composed ONLY of the given sign
def signOnDiagonal(grid, sign):
    if grid[0][0] == sign and grid[1][1] == sign and grid[2][2] == sign:
        return True
    elif grid[0][2] == sign and grid[1][1] == sign and grid[2][0] == sign:
        return True
    return False

  

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if the given sign has WON
def hasSignWon(grid, sign):
    for i in range(len(grid)):
        if signOnDiagonal(grid, sign) or signOnColumn(grid, i, sign) or signOnRow(grid, i, sign):
            return True
    return False


    # TODO ! 
    #  It true if : 
    #  - one of the 2 diagonal is composed of this sign
    #  - or if 1 of the 3 rows is composed of this sign
    #  - or if 1 of the 3 columns is composed of this

    
# MAIN PROGRAM (nothing to change here !)
grid = eval(input())
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")