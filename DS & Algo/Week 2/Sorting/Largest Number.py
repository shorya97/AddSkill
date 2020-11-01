class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if not any(map(bool, nums)):    # this is , if we encounter just zeroes, edge case 
            return '0'
        
        nums = list(map(str, nums))     #  converting it into a string 
        
        if len(nums) <2:
            return "".join(nums)        
        
        def compare(i,j):                                               # comparing the int values after adding and comparing the digits
            return int(nums[i] + nums[j]) > int(nums[j] + nums[i])
        
        for i in range(len(nums)-1):
            j=i+1
            while i<len(nums) and j<len(nums):
                if compare(i,j):
                    pass
                else:
                    nums[j],nums[i] = nums[i],nums[j]
                j+=1
            
        return "".join(nums)
            
