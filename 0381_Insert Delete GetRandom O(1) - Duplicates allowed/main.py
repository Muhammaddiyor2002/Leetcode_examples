import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []  # List to store the numbers
        self.pos = defaultdict(set)  # Dictionary to store the positions of each number

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.pos[val].add(len(self.nums) - 1)
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False

        last_val = self.nums[-1]
        idx = self.pos[val].pop()
        self.nums[idx] = last_val
        self.pos[last_val].add(idx)
        self.pos[last_val].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
