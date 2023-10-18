class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all integers from 1 to maxChoosableInteger is less than desiredTotal,
        # it's impossible to win.
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        # Create a memoization table to store the results of subproblems
        memo = {}
        
        # Define a recursive function to determine if the current player can win
        def canWin(maxChoosableInteger, desiredTotal, used):
            if used in memo:
                return memo[used]
            
            for i in range(maxChoosableInteger, 0, -1):
                bit = 1 << i
                if (used & bit) == 0:
                    # If the current player can choose number i, check if the opponent cannot win
                    if i >= desiredTotal or not canWin(maxChoosableInteger, desiredTotal - i, used | bit):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return canWin(maxChoosableInteger, desiredTotal, 0)
