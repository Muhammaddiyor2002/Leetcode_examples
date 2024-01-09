class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(isConnected, visited, i)
                count += 1
        return count

    def dfs(self, isConnected, visited, i):
        visited.add(i)
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and j not in visited:
                self.dfs(isConnected, visited, j)
