# Steps on how to approach sudoku problem/How to solve it
# Step.1: Pick Empty
# Step.2: Try all numbers
# Step.3: Find a number that works
# Step.4: Repeat
# Step.5: Backtrack

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

#Function
def print_board(bo):

    # For loop to print board//Scan through board
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

print_board(board)