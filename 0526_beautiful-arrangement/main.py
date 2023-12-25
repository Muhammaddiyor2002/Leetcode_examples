
class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        self.used = [False] * (n + 1)
        self.helper(n, 1)
        return self.res

    def helper(self, n, pos):
        if pos > n:
            self.res += 1
            return
        for i in range(1, n + 1):
            if not self.used[i] and (pos % i == 0 or i % pos == 0):
                self.used[i] = True
                self.helper(n, pos + 1)
                self.used[i] = False
