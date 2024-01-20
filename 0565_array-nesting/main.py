class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_length = 0
        for i in range(len(nums)):
            if not visited[i]:
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    length += 1
                max_length = max(max_length, length)
        return max_length
