class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # initialize an empty array
        arr = []
        # start with 1 and increment by 1 until k + 1
        for i in range(1, k + 2):
            # if i is odd, append i // 2 + 1 to the array
            if i % 2 == 1:
                arr.append(i // 2 + 1)
            # if i is even, append k + 2 - i // 2 to the array
            else:
                arr.append(k + 2 - i // 2)
        # append the remaining numbers from k + 2 to n in ascending order
        for i in range(k + 2, n + 1):
            arr.append(i)
        # return the array
        return arr
