class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_sum = 0
        prefix_sum_mod_k = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k

            if prefix_sum in prefix_sum_mod_k:
                if i - prefix_sum_mod_k[prefix_sum] > 1:
                    return True
            else:
                prefix_sum_mod_k[prefix_sum] = i

        return False

# Example usage:
solution = Solution()
nums = [23, 2, 4, 6, 7]
k = 6
result = solution.checkSubarraySum(nums, k)
print(result)  # Output: True
