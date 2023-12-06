class Solution:
    def findLongestWord(self, s: str, d) -> str:
        def is_subsequence(word, target):
            it = iter(target)
            return all(c in it for c in word)

        d.sort(key=lambda x: (-len(x), x))

        for word in d:
            if is_subsequence(word, s):
                return word

        return ""

# Example usage:
solution = Solution()
s = "abpcleafbcd"
d = ["ale","apple","monkey","plea"]
result = solution.findLongestWord(s, d)
print(result)  # Output: "apple"
