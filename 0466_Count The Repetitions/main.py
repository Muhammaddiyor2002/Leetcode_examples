class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len_s1, len_s2 = len(s1), len(s2)
        
        # Handle edge cases
        if len_s1 == 0 or len_s2 == 0 or n1 == 0 or n2 == 0:
            return 0
        
        # Initialize counters and pointers
        count_s1, count_s2 = 0, 0
        ptr_s1, ptr_s2 = 0, 0
        
        while count_s1 < n1:
            if s1[ptr_s1] == s2[ptr_s2]:
                ptr_s2 += 1
                if ptr_s2 == len_s2:
                    ptr_s2 = 0
                    count_s2 += 1
            ptr_s1 += 1
            if ptr_s1 == len_s1:
                ptr_s1 = 0
                count_s1 += 1
        
        return count_s2 // n2
