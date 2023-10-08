class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # Create a dictionary to store sums of pairs from A and B
        sum_AB = {}
        for a in A:
            for b in B:
                sum_AB[a + b] = sum_AB.get(a + b, 0) + 1

        count = 0  # Initialize count of valid quadruplets

        # Iterate through C and D and check if there are complementary sums in sum_AB
        for c in C:
            for d in D:
                if -c - d in sum_AB:
                    count += sum_AB[-c - d]

        return count
