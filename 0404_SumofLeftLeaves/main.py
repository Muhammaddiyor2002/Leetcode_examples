class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        def is_leaf(node):
            return node and not node.left and not node.right

        left_sum = 0

        if is_leaf(root.left):
            left_sum += root.left.val
        else:
            left_sum += self.sumOfLeftLeaves(root.left)

        left_sum += self.sumOfLeftLeaves(root.right)

        return left_sum
