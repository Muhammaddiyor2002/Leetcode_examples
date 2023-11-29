class Solution:
    def change(self, amount: int, coins) -> int:
        # dp[i] represents the number of combinations to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # There is one way to make amount 0 (no coins)

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

# Example usage:
solution = Solution()
amount = 5
coins = [1, 2, 5]
result = solution.change(amount, coins)
print(result)  # Output: 4
