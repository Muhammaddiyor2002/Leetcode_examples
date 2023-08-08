class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        count = 0  # To keep track of the number of arithmetic slices
        current = 0  # To keep track of the length of the current arithmetic slice

        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                current += 1
                count += current
            else:
                current = 0

        return count
