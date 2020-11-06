# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s = t = ListNode(0)
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val < l2.val:
                s.next = l1
                l1 = l1.next
            else:
                s.next = l2
                l2 = l2.next
            s = s.next
        if l1:
            s.next =l1
        if l2:
            s.next =l2
        return t.next
