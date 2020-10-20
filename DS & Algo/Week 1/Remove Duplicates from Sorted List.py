class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp=head
        if temp is None:
            return 
        while temp.next is not None:
            if temp.val == temp.next.val:
                new=temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp=temp.next
        return head
