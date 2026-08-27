# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        done = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    done = True
                else:
                    if done:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
        return True