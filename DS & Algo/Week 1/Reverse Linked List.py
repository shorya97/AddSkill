class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        
        while head: 
            temp = head
            head = head.next
            temp.next = prev      # using temp in such a way to reverse the direction of the pointers 
            prev = temp           # making prev come to the current node so that this same cycle can be repeated 
        return prev
