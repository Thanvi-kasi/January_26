# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Create a value -> index map for inorder traversal
        inorder_map = {value: index for index, value in enumerate(inorder)}
        
        # Pointer for postorder traversal (starting from the end)
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            # Root value is the current postorder index
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build right subtree first
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
