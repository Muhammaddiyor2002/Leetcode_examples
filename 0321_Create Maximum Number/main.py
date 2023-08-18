class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    result.append(nums2[0])
                    nums2 = nums2[1:]
            return result
        
        def getMax(nums, length):
            stack = []
            to_pop = len(nums) - length
            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:length]
        
        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            max_part = merge(getMax(nums1, i), getMax(nums2, k - i))
            max_result = max(max_result, max_part)
        
        return max_result
