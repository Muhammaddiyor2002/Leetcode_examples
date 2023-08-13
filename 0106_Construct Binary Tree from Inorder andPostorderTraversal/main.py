class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root
