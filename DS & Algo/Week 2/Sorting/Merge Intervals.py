class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
            intervals.sort(key=lambda x:x[0])             #sort according to the first item in every element
            i=1
            while i<len(intervals):
                
                if intervals[i][0] <= intervals[i-1][1]:
                    intervals[i-1][0] = min(intervals[i-1][0],intervals[i][0])        # choose the minimum for leftmost element
                    intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])        # choose the maximum for rightmost element
                    
                    intervals.pop(i)   # delete the element after comparison
                else:
                    i+=1
            
            return  intervals
