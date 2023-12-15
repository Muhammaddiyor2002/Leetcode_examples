class Solution:
    def __init__(self, w: List[int]):
        self.pickLst = [0.0]
        sum = 0
        for ele in w:
            sum += ele
        for ele in w:
            self.pickLst.append(self.pickLst[-1] + ele / sum)

    def pickIndex(self) -> int:
        rnd = random.random()
        left = 0
        right = len(self.pickLst) - 1
        result = -1
        while(right > left):
            mid = math.ceil((left + right) / 2)
            if self.pickLst[mid - 1] <= rnd < self.pickLst[mid]:
                result = mid - 1
                break
            if rnd < self.pickLst[mid - 1]:
                right = mid
            elif rnd > self.pickLst[mid]:
                left = mid
        if result == -1:
            raise RuntimeError('cannot find')
        return result
