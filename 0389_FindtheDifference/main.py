class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        
        # Count the occurrences of each character in 's'
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Subtract the occurrences of each character in 't'
        for char in t:
            count[ord(char) - ord('a')] -= 1
            if count[ord(char) - ord('a')] < 0:
                return char
        
        # If no character was found, the added character is the result
        for i in range(26):
            if count[i] < 0:
                return chr(i + ord('a'))
