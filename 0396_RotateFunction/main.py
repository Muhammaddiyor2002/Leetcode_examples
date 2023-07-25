class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        total_sum = sum(A)
        f = sum(i * A[i] for i in range(n))
        max_f = f

        for i in range(n - 1, 0, -1):
            f += total_sum - n * A[i]
            max_f = max(max_f, f)

        return max_f
