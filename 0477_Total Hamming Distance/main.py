class Solution:
    def totalHammingDistance(self, nums) -> int:
        total_distance = 0
        n = len(nums)

        for i in range(32):  # 32 bits in an integer
            count_ones = 0

            # Count the number of set bits at the i-th position
            for num in nums:
                count_ones += (num >> i) & 1

            # Count of zeros at i-th position is (n - count_ones)
            total_distance += count_ones * (n - count_ones)

        return total_distance
