# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:    
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        
        curr =head
        while curr:
            prev_node = dummy
            next_node = prev_node.next
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            next_item = curr.next
            
            curr.next = next_node
            prev_node.next = curr
            
            curr = next_item
            
        return dummy.next
            
            
                
        
        
        
