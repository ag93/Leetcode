
def uniquePaths(rows, cols):
    moves = [[0] * cols for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                moves[row][col] = 1
                print("if", moves)
            else:
                moves[row][col] = moves[row - 1][col] + moves[row][col - 1]
                print("else", moves)
    return moves[rows - 1][cols - 1]


print(uniquePaths(3,3))