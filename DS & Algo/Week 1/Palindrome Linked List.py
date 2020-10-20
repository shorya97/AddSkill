class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s=[]
        p= head
        while p:
            s.append(p.val)
            p=p.next
        return s==s[::-1]
