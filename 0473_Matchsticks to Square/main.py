class Solution:
    def makesquare(self, matchsticks) -> bool:
        if not matchsticks:
            return False
        
        total_length = sum(matchsticks)
        
        if total_length % 4 != 0:
            return False
        
        target_side_length = total_length // 4
        side_lengths = [0] * 4  # Initialize 4 sides of the square

        matchsticks.sort(reverse=True)  # Sort in descending order for efficient exploration
        
        def dfs(index):
            if index == len(matchsticks):
                return all(side == target_side_length for side in side_lengths)
            
            for i in range(4):
                if side_lengths[i] + matchsticks[index] <= target_side_length:
                    side_lengths[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    side_lengths[i] -= matchsticks[index]
            
            return False
        
        return dfs(0)
