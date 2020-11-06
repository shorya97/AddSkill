class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        lmax = 0
        rmax = 0
        low=0
        high = len(height) -1
        while low<=high:
            if height[low] < height[high]:
                if height[low] > lmax:
                    lmax = height[low]  #update max in left 
                else:
                    rain += lmax - height[low]
                low+=1
            else:
                if height[high] > rmax :
                    rmax = height[high]   #update max in right
                else:
                    rain += rmax - height[high]
                high-=1
        return rain                    
                
