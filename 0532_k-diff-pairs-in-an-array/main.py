class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return len([i for i in Counter(nums).values() if i > 1])
        nums = set(nums)
        return sum(num + k in nums for num in nums)

