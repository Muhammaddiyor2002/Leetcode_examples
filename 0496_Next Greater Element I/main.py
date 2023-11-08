class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}  # A dictionary to store the next greater elements
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For elements left in the stack, there's no next greater element
        for num in stack:
            next_greater[num] = -1

        result = [next_greater[num] for num in nums1]
        return result
