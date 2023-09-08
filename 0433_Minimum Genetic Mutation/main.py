from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        # Create a set for faster lookup
        bank = set(bank)
        
        # Define possible mutations
        mutations = ['A', 'C', 'G', 'T']
        
        queue = deque([(start, 0)])  # Start with the initial string and step count
        
        while queue:
            current, steps = queue.popleft()
            
            if current == end:
                return steps  # Mutation reached the target
            
            # Try all possible mutations
            for i in range(len(current)):
                for m in mutations:
                    mutation = current[:i] + m + current[i+1:]
                    if mutation in bank:
                        bank.remove(mutation)
                        queue.append((mutation, steps + 1))
        
        return -1  # No valid mutation sequence found
