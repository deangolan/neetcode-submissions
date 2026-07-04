"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(node):
            if not node:
                return None

            if not cloned.get(node.val):
                cloned[node.val] = Node(node.val)
                for neighbor in node.neighbors:
                    cloned[node.val].neighbors.append(dfs(neighbor))

            return cloned[node.val]
        
        return dfs(node)