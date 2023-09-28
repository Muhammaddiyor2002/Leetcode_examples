class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        # Mark the numbers that are present by negating the value at the corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Add the indices of positive values to the result
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
