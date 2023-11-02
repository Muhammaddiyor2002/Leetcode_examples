class Solution:
    def findSubsequences(self, nums):
        def backtrack(start, path):
            if len(path) >= 2:
                results.append(path[:])
            if start == len(nums):
                return

            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue

                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        results = []
        backtrack(0, [])
        return results
