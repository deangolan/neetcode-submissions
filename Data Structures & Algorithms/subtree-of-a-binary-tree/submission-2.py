# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        def equal(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            return t1.val == t2.val and equal(t1.left, t2.left) and equal(t1.right, t2.right)
        
        def find(t):
            if t is None:
                return False
            elif t.val == subRoot.val:
                if equal(t, subRoot):
                    return True

            return find(t.left) or find(t.right)
        
        return find(root)
