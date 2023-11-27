class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}  # Memoization to store computed results

        def dp(ring_idx, key_idx):
            if key_idx == len(key):
                return 0

            if (ring_idx, key_idx) in memo:
                return memo[(ring_idx, key_idx)]

            result = float('inf')
            for i in range(len(ring)):
                if ring[i] == key[key_idx]:
                    # Calculate steps to rotate to this position
                    clock = (i - ring_idx) % len(ring)
                    counter_clock = (ring_idx - i) % len(ring)

                    # Calculate minimum steps for both directions
                    steps = 1 + min(clock, counter_clock)
                    next_key_idx = key_idx + 1

                    # Recursively calculate steps for the next key
                    steps += dp(i, next_key_idx)

                    # Update result with the minimum steps
                    result = min(result, steps)

            memo[(ring_idx, key_idx)] = result
            return result

        return dp(0, 0)  # Start from the first character of the key

# Example usage:
solution = Solution()
ring = "godding"
key = "gd"
result = solution.findRotateSteps(ring, key)
print(result)  # Output: 4
