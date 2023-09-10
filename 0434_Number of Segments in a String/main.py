class Solution:
    def countSegments(self, s: str) -> int:
        # Initialize a counter for segments
        count = 0
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # If the current character is not a space and the previous character (if exists) is a space, it's the start of a new segment
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        
        return count
