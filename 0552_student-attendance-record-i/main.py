class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        if n == 2:
            return 8
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        res = dp[n]
        for i in range(1, n + 1):
            res += (dp[i - 1] * dp[n - i]) % mod
        return res % mod
