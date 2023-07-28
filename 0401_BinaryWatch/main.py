class Solution:
    def readBinaryWatch(self, turned_on: int) -> List[str]:
        def count_bits(num):
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count

        def backtrack(start, num_ones, hours, minutes):
            if num_ones == turned_on:
                if hours < 12 and minutes < 60:
                    result.append(f"{hours}:{minutes:02}")
                return
            
            for i in range(start, 10):
                if i < 4:
                    new_hours = hours | (1 << i)
                    if new_hours < 12:
                        backtrack(i + 1, num_ones + 1, new_hours, minutes)
                else:
                    new_minutes = minutes | (1 << (i - 4))
                    if new_minutes < 60:
                        backtrack(i + 1, num_ones + 1, hours, new_minutes)

        result = []
        backtrack(0, 0, 0, 0)
        return result
