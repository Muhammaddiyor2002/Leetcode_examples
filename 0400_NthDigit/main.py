class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1

        num = 10 ** (digits - 1) + (n - 1) // digits
        return int(str(num)[(n - 1) % digits])
