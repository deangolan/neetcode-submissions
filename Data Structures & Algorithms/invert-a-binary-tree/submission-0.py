# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node:
                new = TreeNode()
                new.val = node.val
                new.left = invert(node.right)
                new.right = invert(node.left)
                return new
            return None

        return invert(root)
            