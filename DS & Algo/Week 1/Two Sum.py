class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return i,dict[target-nums[i]]
            else:
                dict[nums[i]]=i
