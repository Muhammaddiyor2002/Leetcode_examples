class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]
        
        def dfs(row, col, reachable):
            reachable[row][col] = True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and not reachable[new_row][new_col] and matrix[new_row][new_col] >= matrix[row][col]:
                    dfs(new_row, new_col, reachable)
        
        for row in range(rows):
            dfs(row, 0, pacific_reachable)
            dfs(row, cols - 1, atlantic_reachable)
        
        for col in range(cols):
            dfs(0, col, pacific_reachable)
            dfs(rows - 1, col, atlantic_reachable)
        
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result
