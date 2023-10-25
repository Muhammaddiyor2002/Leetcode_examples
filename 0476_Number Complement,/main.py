class Solution:
    def findComplement(self, num: int) -> int:
        # Find the highest set bit position
        highest_bit = 0
        n = num
        while n > 0:
            highest_bit += 1
            n >>= 1

        # Create a bitmask with all bits set up to the highest set bit
        bitmask = (1 << highest_bit) - 1

        # Take the bitwise NOT of the number and the bitmask to get the complement
        complement = num ^ bitmask

        return complement
