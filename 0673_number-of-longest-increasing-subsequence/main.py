class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # initialize the length and count arrays with 1s
        length = [1] * len(nums)
        count = [1] * len(nums)
        # initialize the max length and the answer
        maxLength = 0
        ans = 0
        # loop through the array from left to right
        for i, num in enumerate(nums):
            # loop through the previous elements
            for j in range(i):
                # if the current element is larger than the previous element
                if num > nums[j]:
                    # update the length and count of the current element
                    if length[i] < length[j] + 1:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
            # update the max length and the answer
            if length[i] > maxLength:
                maxLength = length[i]
                ans = count[i]
            elif length[i] == maxLength:
                ans += count[i]
        # return the answer
        return ans
