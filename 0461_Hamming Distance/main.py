class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Calculate the XOR of the two integers to find differing bits
        xor_result = x ^ y
        hamming_distance = 0
        
        # Count the set bits (1s) in the XOR result
        while xor_result:
            hamming_distance += xor_result & 1
            xor_result >>= 1
        
        return hamming_distance
