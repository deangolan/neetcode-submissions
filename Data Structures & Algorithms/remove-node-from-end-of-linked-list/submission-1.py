# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fst = dummy
        snd = head
        # Move snd n ahead of fst
        i = 0
        while i < n: 
            snd = snd.next
            i += 1

        while snd:
            fst = fst.next
            snd = snd.next

        fst.next = fst.next.next
        return dummy.next