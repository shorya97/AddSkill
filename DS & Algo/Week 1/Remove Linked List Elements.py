class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val==val:
            head=head.next
        cur= head
        while cur and cur.next :
            if cur.next.val == val :
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
