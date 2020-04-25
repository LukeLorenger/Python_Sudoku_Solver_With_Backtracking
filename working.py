# Steps on how to approach sudoku problem/How to solve it
# Step.1: Pick Empty
# Step.2: Try all numbers
# Step.3: Find a number that works
# Step.4: Repeat
# Step.5: Backtrack

# Sudoku: Squares-81, Boxes-9, 3box x 3box grid

# Rules:
# To solve, each row of 9 squares must contain numbers 1-9
# Each column must contain numbers 1-9
# Each box must contain numbers 1-9
# No row, column or box, may repeat any number

# Board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

# algorithm for backtracking
# Using this function recursively, calling this function from inside itself**
def solve(bo):
    
    find = find_empty(bo)
    if not find:
        return True # indicating if solution has been found or not
    else:
        row, col = find

    # Loop through values 1-9, if values are added to board, they will be valid
    for i in range(1,10):
        # If valid, add to board
        if valid(bo, i, (row, col)):
            # add to board
            bo[row][col] = i

            # if we cant finish solution based on value recently added, reset value, try diff value, repeat process recursively
            if solve(bo):
                return True
            # Reset value    
            bo[row][col] = 0

    # If we looped through all numbers, and none are valid, we return false
    return False


# Check in current board is valid, given position
def valid(bo, num, pos):

    # Check row//Loop through every column within the given row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check which box we are in (integer division)
    box_x = pos[1] // 3
    box_y = pos[0] // 3 

    # Loop through box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            # we will loop through box, check if any element in box is equal to what we just added
            # Also making sure we arent going to check the same position we just added in
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True



#Function to print board
def print_board(bo):

    # For loop Scan through board
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            # Printing when I is divisable by 3
            print("- - - - - - - - - - - - - ") 

        # Getting length of rows (rows are 9x9)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                # Printing out vertical line for print separation
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                # (end="") means stay on the same line
                print(str(bo[i][j]) + " ", end="")

# Function for finding empty square(spaces)
# Need to return position of that square to try different elements in
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): # Empty square is defined by 0
            if bo[i][j] == 0:
                return (i, j) # row, column

    return None # If there are no squares equal to zero, return none

print_board(board)
solve(board)
print("_________________________")
print_board(board)
