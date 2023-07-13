import random

class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            # Generate a random index between i and the end of the array
            j = random.randint(i, len(self.nums) - 1)
            # Swap the elements at indices i and j
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
