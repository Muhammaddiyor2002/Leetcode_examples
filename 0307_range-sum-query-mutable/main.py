class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) * 2)
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.nums)):
            self.tree[i + len(self.nums)] = self.nums[i]
        for i in range(len(self.nums) - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i: int, val: int) -> None:
        n = len(self.nums)
        i += n
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            i = i // 2
            self.tree[i] = self.tree[left] + self.tree[right]

    def sumRange(self, i: int, j: int) -> int:
        n = len(self.nums)
        i += n
        j += n
        res = 0
        while i <= j:
            if i % 2 == 1:
                res += self.tree[i]
                i += 1
            if j % 2 == 0:
                res += self.tree[j]
                j -= 1
            i = i // 2
            j = j // 2
        return res
