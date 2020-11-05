class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1]*n
        stack = []
        high = nums.index(max(nums)) if n>0 else 0
        for i in range(high,high-n,-1):
            while len(stack) !=0 and  nums[stack[-1]] <= nums[i]:
                del stack[-1]
            if len(stack) > 0:
                answer[i] = nums[stack[-1]]
            stack.append(i)
        return answer
