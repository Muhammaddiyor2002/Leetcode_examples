class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[1]]
        else:
            return self.getAllRow(numRows - 1)

    def getAllRow(self, numRows):
        if numRows == 0:
            return [[1]]
        ListPrec = self.getAllRow(numRows - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec