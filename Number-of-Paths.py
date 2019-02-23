class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandcount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    grid = self.islandfinder(row,col,grid)
                    grid[row][col]="0"
                    islandcount +=1
        return islandcount

    def islandfinder(self,row,col, grid):
            #right
            if col<(len(grid[0])-1):
                if grid[row][col+1] == "1":
                    grid[row][col+1]="0"
                    self.islandfinder(row,col+1,grid)
            #left
            if col>0:
                if grid[row][col-1] == "1":
                    grid[row][col-1]="0"
                    self.islandfinder(row,col-1,grid)
            #down
            if row<(len(grid)-1):
                if grid[row+1][col] == "1":
                    grid[row+1][col]="0"
                    self.islandfinder(row+1,col,grid)
            #up
            if row>0:
                if grid[row-1][col] == "1":
                    grid[row-1][col]="0"
                    self.islandfinder(row-1,col,grid)
            return grid