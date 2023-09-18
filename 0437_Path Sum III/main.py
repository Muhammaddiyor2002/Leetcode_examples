# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        
        # Helper function for counting paths
        def count_paths(node, target):
            if not node:
                return 0
            
            # Check if the current node value equals the target
            current_paths = 1 if node.val == target else 0
            
            # Recursively check left and right subtrees
            current_paths += count_paths(node.left, target - node.val)
            current_paths += count_paths(node.right, target - node.val)
            
            return current_paths
        
        # Use DFS to traverse the tree and count paths
        def dfs(node):
            if not node:
                return 0
            
            # Start counting paths from the current node
            paths_from_current = count_paths(node, targetSum)
            
            # Recursively traverse left and right subtrees
            left_paths = dfs(node.left)
            right_paths = dfs(node.right)
            
            # Total paths from this subtree
            total_paths = paths_from_current + left_paths + right_paths
            
            return total_paths
        
        # Start the DFS traversal from the root
        return dfs(root)
