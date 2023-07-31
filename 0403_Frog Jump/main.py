class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        dp = {}  # Dictionary to store the possible jumps from each stone

        for stone in stones:
            dp[stone] = set()

        dp[1].add(1)  # The frog can start with a jump of 1 unit from the first stone

        for stone in stones[:-1]:
            for jump in dp[stone]:
                for next_jump in [jump - 1, jump, jump + 1]:
                    if next_jump > 0 and stone + next_jump in dp:
                        dp[stone + next_jump].add(next_jump)

        return len(dp[stones[-1]]) > 0
