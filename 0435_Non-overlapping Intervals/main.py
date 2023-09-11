class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end points
        intervals.sort(key=lambda x: x[1])
        
        count = 1  # At least one interval will be non-overlapping
        end = intervals[0][1]  # Initialize the end of the current non-overlapping interval
        
        for interval in intervals[1:]:
            if interval[0] >= end:
                # If the start of the current interval is greater than or equal to the end of the previous non-overlapping interval
                # it can be included as non-overlapping
                count += 1
                end = interval[1]
        
        # Calculate the number of intervals to be removed to get non-overlapping intervals
        # The total number of intervals minus non-overlapping intervals
        removals = len(intervals) - count
        
        return removals
