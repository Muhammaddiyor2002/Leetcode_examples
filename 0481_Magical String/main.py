class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0

        magical_str = [1, 2, 2]
        ptr = 2

        while len(magical_str) < n:
            next_val = 3 - magical_str[-1]
            count = magical_str[ptr]

            magical_str.extend([next_val] * count)
            ptr += 1

        return magical_str[:n].count(1)
