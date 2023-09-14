import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []

        n = len(intervals)
        result = [-1] * n  # Initialize the result array with -1

        # Create a list of intervals with the start and original index
        start_intervals = [(interval[0], i) for i, interval in enumerate(intervals)]

        # Sort the start_intervals by start time
        start_intervals.sort()

        for i in range(n):
            end = intervals[i][1]

            # Perform binary search to find the right interval
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if start_intervals[mid][0] >= end:
                    result[i] = start_intervals[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

        return result
