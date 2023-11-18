class Solution:
    def findRelativeRanks(self, nums):
        ranked_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        result = [""] * len(nums)

        for i, (index, _) in enumerate(ranked_nums):
            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)

        return result
