class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sumval = 0
        root = curr = ListNode(0)
        while l1 or l2 or sumval:
            if l1:
                sumval += l1.val
                l1 = l1.next
            if l2:
                sumval += l2.val
                l2 = l2.next
            curr.next = curr = ListNode(sumval % 10)
            sumval //= 10
        return root.next
