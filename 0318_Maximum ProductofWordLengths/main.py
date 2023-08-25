class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_masks = [0] * len(words)
        
        for i, word in enumerate(words):
            for char in word:
                bit_masks[i] |= 1 << (ord(char) - ord('a'))
        
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bit_masks[i] & bit_masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
