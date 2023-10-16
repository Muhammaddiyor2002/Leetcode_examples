class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array to find the median

        median = nums[len(nums) // 2]  # Find the median element

        # Calculate the sum of absolute differences between each element and the median
        min_moves = 0
        for num in nums:
            min_moves += abs(num - median)

        return min_moves
