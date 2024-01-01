# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, total):
            if not node:
                return total
            node.val += dfs(node.right, total)
            return dfs(node.left, node.val)
        dfs(root, 0)
        return root
