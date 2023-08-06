class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def countSubarrays(max_sum):
            count = 1
            current_sum = 0

            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    count += 1
                    current_sum = num

            return count

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            subarray_count = countSubarrays(mid)

            if subarray_count > m:
                left = mid + 1
            else:
                right = mid

        return left
