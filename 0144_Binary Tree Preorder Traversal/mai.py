class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorder(root, result)
        return result
    
    def preorder(self, node, result):
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
