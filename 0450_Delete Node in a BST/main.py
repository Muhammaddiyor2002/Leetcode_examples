# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root  # Base case: the tree is empty

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with the key found, delete it
            if not root.left:
                return root.right  # Case 1: Node has no left child
            elif not root.right:
                return root.left  # Case 2: Node has no right child

            # Case 3: Node has two children, find the inorder successor (smallest in right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        # Helper function to find the minimum node in a BST
        while node.left:
            node = node.left
        return node
