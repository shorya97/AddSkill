class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        answer=[]    #initialize empty array
        while i<len(intervals) and newInterval[0]>intervals[i][0]: #append elements which are less than newInterval
                answer.append(intervals[i])
                i+=1
                
        if not answer or answer[-1][1] < newInterval[0]:  #last number in answer is smaller than newInterval[0], if true , append , else move forward 
            answer.append(newInterval)
        else:
            answer[-1][1] = max(answer[-1][1],newInterval[1])
            
        while i<len(intervals):                           #add the remaining elements by constantly checking the over lapping intervals
            if answer[-1][1] < intervals[i][0]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1],intervals[i][1])
            i+=1
        return answer
                
