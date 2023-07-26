class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num == 1:
                return 0
            if num in memo:
                return memo[num]

            if num % 2 == 0:
                memo[num] = 1 + dfs(num // 2)
            else:
                memo[num] = 1 + min(dfs(num + 1), dfs(num - 1))

            return memo[num]

        return dfs(n)
