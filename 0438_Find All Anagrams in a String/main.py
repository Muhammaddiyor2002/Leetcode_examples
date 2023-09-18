from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1

            if s_counter == p_counter:
                result.append(i - len(p) + 1)

            if s_counter[s[i - len(p) + 1]] == 1:
                del s_counter[s[i - len(p) + 1]]
            else:
                s_counter[s[i - len(p) + 1]] -= 1

        return result
