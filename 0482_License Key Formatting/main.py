class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # Remove '-' characters and convert the string to uppercase
        S = S.replace("-", "").upper()
        
        # Calculate the length of the first group
        first_group_len = len(S) % K
        
        # Initialize the result with the first group (if it's not empty)
        result = S[:first_group_len]
        
        # Add '-' and groups of K characters to the result
        for i in range(first_group_len, len(S), K):
            if result:
                result += "-"
            result += S[i:i + K]
        
        return result
