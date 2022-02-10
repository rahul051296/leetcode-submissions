class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, row, col):
            rl = len(grid) - 1
            cl = len(grid[0]) - 1
            if not (0 <= row <= rl and 0<= col <= cl) or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
            
        if len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1  
                    dfs(grid,i,j)
        return count

            
       
        
        