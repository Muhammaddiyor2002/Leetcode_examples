class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        dp = [defaultdict(int) for _ in range(n)]  # dp[i] will store the count of arithmetic slices ending at nums[i]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1  # Increment the count for the current difference
                
                # Add the count to the total
                total += dp[j][diff]

        return total
