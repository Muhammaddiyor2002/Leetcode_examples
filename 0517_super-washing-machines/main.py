class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines) != 0:
            return -1
        avg = total // len(machines)
        ans, cnt = 0, 0
        for m in machines:
            cnt += m - avg
            ans = max(ans, abs(cnt), m - avg)
        return ans
