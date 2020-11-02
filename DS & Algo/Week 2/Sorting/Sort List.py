# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #using merge sort
        #midpoint
        if not head or not head.next:
            return head
        mid = self.midPoint(head)     
        #recursive left and right
        left = self.sortList(head)
        right = self.sortList(mid)
        #merge
        return self.merge(left,right)
    
    def merge(self,left,right):
        
        dummy = cur = ListNode(0)
        
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left= left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
                
        cur.next = left or right
        return dummy.next
        
        
    def midPoint(self,head):
        #split linked list
        slow=head
        fast=head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next                 ## mid point is slow.next
        slow.next = None                ## split right and left
        return mid                      ## midpoint is the new head
