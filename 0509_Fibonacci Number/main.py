class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        fib_nums = [0] * (n + 1)
        fib_nums[1] = 1

        for i in range(2, n + 1):
            fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]

        return fib_nums[n]
