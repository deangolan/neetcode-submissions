"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if not node:
                    continue
                if q and i < n-1:
                    node.next = q[0]
                q.append(node.left)
                q.append(node.right)
        return root