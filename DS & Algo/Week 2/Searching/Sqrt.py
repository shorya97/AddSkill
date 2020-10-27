class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0
        if x==1:
            return 1
        
        l=2
        h=x//2
        while l<=h:
            m=(l+h)//2
            if m**2==x:
                return m
            elif m**2<x:
                l=m+1
            else:
                h=m-1
        return h
                
