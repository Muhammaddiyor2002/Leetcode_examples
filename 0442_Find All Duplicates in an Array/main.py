class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1  # Get the index of the current number (1-based)
            if nums[index] < 0:
                duplicates.append(abs(num))  # If the number at this index is negative, it's a duplicate
            else:
                nums[index] = -nums[index]  # Mark the number as seen by making it negative
        
        return duplicates
