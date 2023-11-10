import random

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.weights = [((x2 - x1 + 1) * (y2 - y1 + 1)) for x1, y1, x2, y2 in rects]

    def pick(self):
        x1, y1, x2, y2 = random.choices(self.rects, weights=self.weights)[0]
        return [random.randint(x1, x2), random.randint(y1, y2)]
