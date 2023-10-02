class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character in the string
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        # Sort the characters by their frequency in descending order
        sorted_chars = sorted(s, key=lambda char: (-frequency[char], char))

        # Join the sorted characters to form the final result
        return ''.join(sorted_chars)
