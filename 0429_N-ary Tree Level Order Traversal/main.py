# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_vals = []
            next_level = []
            
            for node in queue:
                level_vals.append(node.val)
                next_level.extend(node.children)
            
            result.append(level_vals)
            queue = next_level
        
        return result
