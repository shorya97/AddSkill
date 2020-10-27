class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)-1 
        low = 0
        high = n
        while low<=high:
            mid=(low+high)//2
            
            
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
            
        
        if not nums:
            return 0
        if target>nums[high]:
            return high+1
        if target<nums[low]:
            return low       
