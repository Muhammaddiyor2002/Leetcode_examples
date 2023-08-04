import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        min_heap = []  # Priority queue to store cells in ascending order of height

        # Add the boundary cells to the priority queue and mark them as visited
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # Define the four possible directions to move
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        total_water = 0
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    # The amount of water that can be trapped is based on the difference in heights
                    total_water += max(0, height - heightMap[new_x][new_y])
                    # The height of the cell to visit next is the maximum of the current cell height and the height we have traversed so far
                    heapq.heappush(min_heap, (max(height, heightMap[new_x][new_y]), new_x, new_y))
                    visited[new_x][new_y] = True

        return total_water
