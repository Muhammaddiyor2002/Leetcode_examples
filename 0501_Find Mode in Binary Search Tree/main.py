class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        if not root:
            return []

        counter = {}
        self.traverse(root, counter)

        max_freq = max(counter.values())
        modes = [key for key, freq in counter.items() if freq == max_freq]
        return modes

    def traverse(self, node, counter):
        if not node:
            return

        self.traverse(node.left, counter)
        counter[node.val] = counter.get(node.val, 0) + 1
        self.traverse(node.right, counter)
