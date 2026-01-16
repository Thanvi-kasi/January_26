# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the leftmost node of each level
        leftmost = root
        
        while leftmost.left:
            current = leftmost
            while current:
                # Connect left child to right child
                current.left.next = current.right
                
                # Connect right child to next subtree's left child
                if current.next:
                    current.right.next = current.next.left
                
                current = current.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root
