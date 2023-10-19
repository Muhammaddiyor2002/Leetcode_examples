class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        
        # Create a dictionary to store the maximum length of valid substrings ending with each character
        max_lengths = {}
        
        length, result = 0, 0
        
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25):
                length += 1
            else:
                length = 1

            # Update the maximum length for the current character
            max_lengths[p[i]] = max(max_lengths.get(p[i], 0), length)

        # Sum the maximum lengths for all characters to get the result
        result = sum(max_lengths.values())

        return result
