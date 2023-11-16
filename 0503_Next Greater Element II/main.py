class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        # Iterate twice through the circular array
        for i in range(2 * n):
            index = i % n

            while stack and nums[index] > nums[stack[-1]]:
                # Update the result for elements with a next greater element
                result[stack.pop()] = nums[index]

            stack.append(index)

        return result
