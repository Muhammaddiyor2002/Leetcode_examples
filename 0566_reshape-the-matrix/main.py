class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        flat = [num for row in nums for num in row]
        return [flat[i*c:(i+1)*c] for i in range(r)]
