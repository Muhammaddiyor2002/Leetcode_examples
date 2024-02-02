class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # define a helper function to count how many numbers are smaller than or equal to x in the table
        def count(x):
            # initialize the counter
            c = 0
            # loop through each row
            for i in range(1, m + 1):
                # add the minimum of x // i or n to the counter
                c += min(x // i, n)
            # return the counter
            return c
        
        # initialize the low and high pointers
        low = 1
        high = m * n
        # binary search for the kth smallest number
        while low < high:
            # calculate the mid point
            mid = (low + high) // 2
            # if the count of numbers smaller than or equal to mid is less than k, move the low pointer to mid + 1
            if count(mid) < k:
                low = mid + 1
            # otherwise, move the high pointer to mid
            else:
                high = mid
        # return the low pointer as the answer
        return low
