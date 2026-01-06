# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Case 1: Both trees are empty
        if not p and not q:
            return True
        
        # Case 2: One tree is empty and the other is not
        if not p or not q:
            return False
        
        # Case 3: Both trees are non-empty, check current node and recurse for left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # Case 4: Values are different at the current node
        return False
