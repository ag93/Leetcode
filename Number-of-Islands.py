from collections import deque

class Solution:
    def numIslands(grid):
        
        islands = 0
        rowsLen = len(grid)
        colLen = len(grid[0])
        
        def bfs(grid, i, j):
            grid[i][j] = "-1"
            queue = deque([(i,j)])

            while len(queue)!=0:
                row, col = queue.popleft()
                possibeEdges = [(1,0),(0,1),(-1,0),(0,-1)]

                for possibleRow, possibeCol in possibeEdges:
                    currentRow = row + possibleRow
                    currentCol = col + possibeCol

                    if (currentRow in range(rowsLen) and currentCol in range(colLen) and grid[currentRow][currentCol] == "1"):
                        grid[currentRow][currentCol] = "-1"
                        queue.append((currentRow, currentCol))
                        
        
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(grid, i,j)
        return islands


    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    result = str(numIslands(grid))

    print("Total Number of Islands = " + result)