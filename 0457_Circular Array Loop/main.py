class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Helper function to get the next index considering circular movement
        def get_next_index(current_index):
            return (current_index + nums[current_index]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue  # Skip elements that are part of a known non-loop cycle
            
            slow = i
            fast = i
            
            while nums[slow] * nums[get_next_index(fast)] > 0:
                slow = get_next_index(slow)
                fast = get_next_index(get_next_index(fast))
                
                if slow == fast:
                    if slow == get_next_index(slow):
                        break  # The cycle contains only one element and is not a valid loop
                    return True
                
            # Mark the current cycle elements as zero (not part of a loop)
            j = i
            while nums[j] * nums[get_next_index(j)] > 0:
                tmp = get_next_index(j)
                nums[j] = 0
                j = tmp

        return False
