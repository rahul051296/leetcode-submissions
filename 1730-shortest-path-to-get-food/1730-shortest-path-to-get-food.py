class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        row_size = len(grid) - 1
        col_size = len(grid[0]) - 1
        directions = [(0, -1),(-1, 0), (0, 1),(1, 0)]
        
        def get_neighbors(row, col):
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff
                if not (0 <= new_row <= row_size and 0<=new_col<=col_size):
                    continue
                if grid[new_row][new_col] == "X":
                    continue
                yield((new_row, new_col))
         
        queue = deque()
        
        
        for i in range(row_size+1):
            for j in range(col_size+1):
                if grid[i][j] == "*":
                    queue.append((i, j, 1))   
        
        
        while queue:
            curr_row, curr_col, steps = queue.popleft()
            for r, c in get_neighbors(curr_row, curr_col):
                if grid[r][c] == '#':
                    return steps
                grid[r][c] = 'X'
                queue.append((r, c, steps+1))
        return - 1
