# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return (True, 0)
            bl, hl = traverse(node.left) 
            br, hr = traverse(node.right)
            h = max(hl, hr) + 1
            b = abs(hl - hr) <= 1 and bl and br
            return (b, h)
        
        return traverse(root)[0]