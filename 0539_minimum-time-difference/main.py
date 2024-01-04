class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def getMinute(t):
            h, m = t.split(":")
            return int(h) * 60 + int(m)
        timePoints = sorted(map(getMinute, timePoints))
        mn = sys.maxsize
        for i in range(len(timePoints) - 1):
            mn = min(mn, timePoints[i + 1] - timePoints[i])
            if mn == 0:
                return 0
        return min(mn, 1440 + timePoints[0] - timePoints[-1])
