"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        refs = defaultdict(lambda: Node(0))
        cur = head
        while cur:
            refs[cur].val = cur.val
            if cur.next:
                refs[cur].next = refs[cur.next]
            if cur.random:
                refs[cur].random = refs[cur.random]
            cur = cur.next

        return refs[head]