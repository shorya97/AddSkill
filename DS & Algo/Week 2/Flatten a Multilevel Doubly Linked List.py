"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dummy = Node(0)   #keep track of what the head is going to be 
        cur = dummy 
        stack = [head]
        while stack:
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None
            cur = tmp
        dummy.next.prev = None
        return dummy.next
            
            
        
        
