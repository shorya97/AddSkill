class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
      
        
        def first_occurence(nums,target):
            n = len(nums)-1
            start = 0
            res = -1
            end = n
            while start<=end:
                mid=(start+end)//2       #Binary Search Logic
                if target==nums[mid]:
                    res=mid
                    end=mid-1
                elif target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return res

        def last_occurence(nums,target):
            n = len(nums)-1
            start = 0
            res = -1
            end = n
            while start<=end:
                mid=(start+end)//2
                if target==nums[mid]:
                    res=mid
                    start=mid+1
                elif target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return res
        
        return [first_occurence(nums,target),last_occurence(nums,target)]
    
        
                
                
        
        
