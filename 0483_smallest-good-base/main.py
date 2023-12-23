class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        for m in range(63, 1, -1):
            left, right = 2, num - 1
            while left <= right:
                mid = (left + right) // 2
                cal = (mid ** m - 1) // (mid - 1)
                if cal == num:
                    return str(mid)
                elif cal < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return str(num - 1)
