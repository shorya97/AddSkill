class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=j=1
        if len(nums)<=1:
            return len(nums)
        while i<len(nums):
            if nums[i] != nums[i-1]:  #unique element found
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
                
