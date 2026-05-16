"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}
        def clone(node):
            new = Node(node.val)
            cloned[node.val] = new
            for n in node.neighbors:
                if n.val not in cloned:
                    clone(n)
                new.neighbors.append(cloned[n.val])
            return new

        return clone(node)
