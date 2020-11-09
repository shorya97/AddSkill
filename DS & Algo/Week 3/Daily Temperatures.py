class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result=[0]*len(T)
        stack=[]
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                result[stack.pop()] = i - stack[-1]
            stack.append(i)                    
        return result
