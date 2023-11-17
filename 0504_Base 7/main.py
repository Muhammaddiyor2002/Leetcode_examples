class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        result = ""
        sign = "" if num >= 0 else "-"
        num = abs(num)

        while num > 0:
            # Build the base 7 representation from the remainders
            result = str(num % 7) + result
            num //= 7

        return sign + result
