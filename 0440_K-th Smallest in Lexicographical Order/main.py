class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1  # Start from 1
        k -= 1  # Decrement k by 1 because 1 is the first number
        while k > 0:
            steps = self.count_steps(n, current, current + 1)
            if k >= steps:  # If k is greater than or equal to steps, move to the next number
                current += 1
                k -= steps
            else:  # Otherwise, move to the child node (next number with a common prefix)
                current *= 10
                k -= 1
        return current
    
    def count_steps(self, n, n1, n2):
        # Count the number of integers between n1 and n2 in the range [1, n]
        steps = 0
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
