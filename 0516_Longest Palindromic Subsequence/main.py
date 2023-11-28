class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Initialize a 2D DP table
        dp = [[0] * n for _ in range(n)]

        # Every character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the DP table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and length == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

# Example usage:
solution = Solution()
s = "bbbab"
result = solution.longestPalindromeSubseq(s)
print(result)  # Output: 4
