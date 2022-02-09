class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r = len(grid) - 1
        c = len(grid[0]) - 1
        if r + 1 == 1 and c+1 == 1:
            return 0
        directions = [(0,-1), (-1,0), (0, 1), (1, 0)]
        
        def get_neighbors(row, col):
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff
                
                if not (0 <= new_row <= r and 0 <= new_col <= c):
                    continue
                yield((new_row, new_col))
                
        queue = deque()
        
        queue.append((0, 0, 1, k))
        visited = set([(0, 0, k)])
        while queue:
            cur_row, cur_col, steps, eliminate = queue.popleft()
            
            for n_r, n_c in get_neighbors(cur_row, cur_col):
                if grid[n_r][n_c] == 1 and eliminate > 0 and (n_r, n_c, eliminate - 1) not in visited:
                    visited.add((n_r, n_c, eliminate - 1))
                    queue.append((n_r, n_c, steps+1, eliminate-1))
                if grid[n_r][n_c] == 0 and (n_r, n_c, eliminate - 1) not in visited:
                    if n_r == r and n_c == c:
                        return steps
                    visited.add((n_r, n_c, eliminate - 1))
                    queue.append((n_r, n_c, steps+1, eliminate))
        return -1 
                    