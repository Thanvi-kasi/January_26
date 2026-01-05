# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # This will store the nodes that are swapped
        first = second = prev = None
        
        # Helper function for in-order traversal
        def inorder(node):
            nonlocal first, second, prev
            
            if node is None:
                return
            
            # In-order traversal: visit left subtree
            inorder(node.left)
            
            # If this node's value is less than the previous node's value, it's a violation
            if prev and prev.val > node.val:
                # First violation: 'first' is the previous node
                if not first:
                    first = prev
                # Second violation: 'second' is the current node
                second = node
            
            # Update the previous node to the current node
            prev = node
            
            # In-order traversal: visit right subtree
            inorder(node.right)
        
        # Perform in-order traversal to find the swapped nodes
        inorder(root)
        
        # Swap the values of the two nodes
        if first and second:
            first.val, second.val = second.val, first.val
