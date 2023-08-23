class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, indices, start, end, result):
            if start >= end:
                return
            
            mid = start + (end - start) // 2
            mergeSort(arr, indices, start, mid, result)
            mergeSort(arr, indices, mid + 1, end, result)
            
            merged = []
            p1, p2 = start, mid + 1
            count = 0
            
            while p1 <= mid and p2 <= end:
                if arr[indices[p1]] > arr[indices[p2]]:
                    merged.append(indices[p2])
                    p2 += 1
                    count += 1
                else:
                    merged.append(indices[p1])
                    result[indices[p1]] += count
                    p1 += 1
            
            while p1 <= mid:
                merged.append(indices[p1])
                result[indices[p1]] += count
                p1 += 1
            
            while p2 <= end:
                merged.append(indices[p2])
                p2 += 1
            
            indices[start:end + 1] = merged
        
        n = len(nums)
        result = [0] * n
        indices = list(range(n))
        mergeSort(nums, indices, 0, n - 1, result)
        
        return result
