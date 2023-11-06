class Solution:
    def reversePairs(self, nums) -> int:
        def mergeSort(nums, left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            merge(nums, left, mid, right)
            
            return count
        
        def merge(nums, left, mid, right):
            merged = [0] * (right - left + 1)
            i, j, k = left, mid + 1, 0
            
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    merged[k] = nums[i]
                    i += 1
                else:
                    merged[k] = nums[j]
                    j += 1
                k += 1
            
            while i <= mid:
                merged[k] = nums[i]
                i += 1
                k += 1
            
            while j <= right:
                merged[k] = nums[j]
                j += 1
                k += 1
            
            for i in range(left, right + 1):
                nums[i] = merged[i - left]
        
        if not nums:
            return 0
        
        return mergeSort(nums, 0, len(nums) - 1)
