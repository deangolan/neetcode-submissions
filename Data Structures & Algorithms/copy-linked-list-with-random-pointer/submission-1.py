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
            
        refs = {}
        cur = head
        while cur:
            if cur not in refs:
                new = Node(cur.val)
                refs[cur] = new
            
            if cur.next:
                if cur.next in refs:
                    refs[cur].next = refs[cur.next]
                else:
                    new = Node(cur.next.val)
                    refs[cur.next] = new
                    refs[cur].next = refs[cur.next]
            
            if cur.random:
                if cur.random in refs:
                    refs[cur].random = refs[cur.random]
                else:
                    new = Node(cur.random.val)
                    refs[cur.random] = new
                    refs[cur].random = refs[cur.random]

            cur = cur.next

        return refs[head]