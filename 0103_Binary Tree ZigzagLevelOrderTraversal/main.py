class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        zigzag = False  # Flag to indicate zigzag direction
        
        while queue:
            level_values = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.pop(0)
                if zigzag:
                    level_values.insert(0, node.val)  # Insert at the beginning for zigzag
                else:
                    level_values.append(node.val)  # Append at the end for regular order

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
            zigzag = not zigzag
        
        return result
