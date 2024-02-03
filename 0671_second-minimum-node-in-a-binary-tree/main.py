class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # initialize the first and second minimum values as the root value and -1
        first = second = root.val
        # define a helper function to traverse the tree
        def dfs(node):
            # use the nonlocal keyword to access the outer variables
            nonlocal first, second
            # base case: if the node is None, return
            if not node:
                return
            # recursive case: if the node value is smaller than the first minimum, update both first and second
            if node.val < first:
                first, second = node.val, first
            # recursive case: if the node value is between the first and second minimum, update the second
            elif first < node.val < second or second == first:
                second = node.val
            # recursive case: traverse the left and right subtrees
            dfs(node.left)
            dfs(node.right)
        # call the helper function with the root node
        dfs(root)
        # return the second minimum value or -1 if it does not exist
        return second if second > first else -1
