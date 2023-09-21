class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n  # Initialize binary search boundaries
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the midpoint of the current range
            total_coins = (mid * (mid + 1)) // 2  # Calculate the total coins in the first 'mid' rows
            
            if total_coins == n:
                return mid  # If we have exactly n coins, return the number of rows
            
            if total_coins < n:
                left = mid + 1  # If we have fewer coins, increase the search range to the right
            else:
                right = mid - 1  # If we have more coins, decrease the search range to the left
        
        return right  # When the binary search ends, 'right' is the largest number of rows that fits within 'n'
