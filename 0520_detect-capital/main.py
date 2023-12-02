class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All uppercase
        if word.isupper():
            return True
        
        # Case 2: All lowercase
        if word.islower():
            return True
        
        # Case 3: Only first letter uppercase
        if word[0].isupper() and word[1:].islower():
            return True
        
        # All other cases are incorrect
        return False

# Example usage:
solution = Solution()
word = "USA"
result = solution.detectCapitalUse(word)
print(result)  # Output: True
