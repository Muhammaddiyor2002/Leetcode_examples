# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 0:
            return None
        if n == 1:
            return Node(val=grid[0][0], isLeaf=True)
        
        def isLeaf(x, y, size):
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != grid[x][y]:
                        return False
            return True
        
        def buildTree(x, y, size):
            if size == 1:
                return Node(val=grid[x][y], isLeaf=True)
            
            half = size // 2
            topLeft = buildTree(x, y, half)
            topRight = buildTree(x, y + half, half)
            bottomLeft = buildTree(x + half, y, half)
            bottomRight = buildTree(x + half, y + half, half)
            
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
                    topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(val=topLeft.val, isLeaf=True)
            
            return Node(isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
        
        return buildTree(0, 0, n)
