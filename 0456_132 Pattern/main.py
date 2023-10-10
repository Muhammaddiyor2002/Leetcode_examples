class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_left = [nums[0]]  # Store the minimum value on the left of each element
        for i in range(1, n):
            min_left.append(min(min_left[-1], nums[i]))

        stack = []  # Use a stack to track potential values for nums[k]

        for j in range(n - 1, -1, -1):
            if nums[j] > min_left[j]:
                while stack and stack[-1] <= min_left[j]:
                    stack.pop()  # Remove values that cannot be used as nums[k]
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
