class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num < first_max and num > second_max:
                third_max = second_max
                second_max = num
            elif num < second_max and num > third_max:
                third_max = num

        return third_max if third_max != float('-inf') else first_max
