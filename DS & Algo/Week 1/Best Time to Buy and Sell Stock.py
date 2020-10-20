class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans=0
        minimum = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum = prices[i]
            ans= max(ans,prices[i]-minimum)
        return ans
