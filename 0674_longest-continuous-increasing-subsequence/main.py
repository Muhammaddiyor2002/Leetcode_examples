class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # initialize the current and maximum length as 0
        curr = maxLen = 0
        # loop through the array
        for i in range(len(nums)):
            # if the current element is larger than the previous element, increase the current length by 1
            if i == 0 or nums[i] > nums[i - 1]:
                curr += 1
            # otherwise, reset the current length to 1
            else:
                curr = 1
            # update the maximum length with the current length
            maxLen = max(maxLen, curr)
        # return the maximum length
        return maxLen
