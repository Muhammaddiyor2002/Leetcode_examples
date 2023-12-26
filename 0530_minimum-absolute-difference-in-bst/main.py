class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min_diff = float('inf')
        self.inorder(root)
        return self.min_diff

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.prev:
            self.min_diff = min(self.min_diff, node.val - self.prev.val)
        self.prev = node
        self.inorder(node.right)
