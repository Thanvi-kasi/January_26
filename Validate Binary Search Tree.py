# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function to check the validity of the tree within bounds
        def helper(node, low, high):
            if not node:
                return True  # An empty tree is a valid BST
            if node.val <= low or node.val >= high:
                return False  # Node value must be within the valid range
            # Recursively check the left and right subtrees
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        # Call the helper with the initial range of valid values (-inf to +inf)
        return helper(root, float('-inf'), float('inf'))
