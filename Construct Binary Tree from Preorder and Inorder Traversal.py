# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Map each value to its index in inorder for O(1) lookup
        inorder_index = {value: i for i, value in enumerate(inorder)}
        
        self.pre_idx = 0  # Pointer for preorder traversal
        
        def helper(left, right):
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Split inorder list
            index = inorder_index[root_val]
            
            # Build left and right subtrees
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)
