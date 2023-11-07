class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0

        total_time = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration

        for time in timeSeries[1:]:
            if time <= end:
                # Overlapping interval
                end = time + duration
            else:
                # Non-overlapping interval
                total_time += end - start
                start = time
                end = time + duration

        total_time += end - start
        return total_time
