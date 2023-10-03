class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the intervals by their end points
        points.sort(key=lambda x: x[1])

        arrows = 1  # Initialize with one arrow since we have to shoot at least once
        prev_end = points[0][1]

        for start, end in points:
            if start > prev_end:
                # If the current balloon starts after the previous end point, we need another arrow
                arrows += 1
                prev_end = end

        return arrows
