class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # For each land cell, check its neighbors
                    perimeter += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        perimeter -= 2  # Subtract 2 for top neighbor
                    if col > 0 and grid[row][col - 1] == 1:
                        perimeter -= 2  # Subtract 2 for left neighbor

        return perimeter
