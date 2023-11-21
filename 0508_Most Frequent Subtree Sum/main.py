class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        sum_count = {}  # Dictionary to store subtree sums and their frequencies
        self.calculateSubtreeSum(root, sum_count)

        max_freq = max(sum_count.values())
        frequent_sums = [key for key, freq in sum_count.items() if freq == max_freq]
        return frequent_sums

    def calculateSubtreeSum(self, node, sum_count):
        if not node:
            return 0

        left_sum = self.calculateSubtreeSum(node.left, sum_count)
        right_sum = self.calculateSubtreeSum(node.right, sum_count)

        subtree_sum = node.val + left_sum + right_sum
        sum_count[subtree_sum] = sum_count.get(subtree_sum, 0) + 1

        return subtree_sum
