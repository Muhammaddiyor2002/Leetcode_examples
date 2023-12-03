class Solution:
    def findLUSlength(self, strs) -> int:
        def is_subsequence(s1, s2):
            it = iter(s2)
            return all(c in it for c in s1)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            all_smaller = all(not is_subsequence(strs[i], strs[j]) for j in range(len(strs)) if i != j)
            if all_smaller:
                return len(strs[i])

        return -1  # No uncommon subsequence found

# Example usage:
solution = Solution()
strs = ["aba", "cdc", "eae"]
result = solution.findLUSlength(strs)
print(result)  # Output: 3
