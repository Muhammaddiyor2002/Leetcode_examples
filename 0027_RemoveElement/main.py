class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):  # loop how many val is in the list
            nums.remove(val)  # remove each val one by one
        return len(nums)  # return len of nums