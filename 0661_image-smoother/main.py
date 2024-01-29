class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count, total = 0, 0
                for ni, nj in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if 0 <= ni < m and 0 <= nj < n:
                        count += 1
                        total += M[ni][nj]
                res[i][j] = total // count
        return res
