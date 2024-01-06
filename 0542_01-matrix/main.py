class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = collections.deque([(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0])
        dist = [[0] * n for _ in range(m)]
        visited = set(q)
        while q:
            i, j = q.popleft()
            for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[i][j] + 1
                    visited.add((ni, nj))
                    q.append((ni, nj))
        return dist
