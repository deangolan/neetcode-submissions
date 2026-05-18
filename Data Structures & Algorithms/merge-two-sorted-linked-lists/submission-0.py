# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val > ptr2.val:
                cur.next = ptr2
                ptr2 = ptr2.next
            else:
                cur.next = ptr1
                ptr1 = ptr1.next
            cur = cur.next
        
        while ptr1:
            cur.next = ptr1
            ptr1 = ptr1.next
            cur = cur.next
        
        while ptr2:
            cur.next = ptr2
            ptr2 = ptr2.next
            cur = cur.next

        return res.next

