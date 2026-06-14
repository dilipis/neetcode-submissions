class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1. Set initial values. MaxProfit = 0
        maxProfit = 0

        # 2. Loop through list. Find higher index which is more than current list item
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i] 


        
        # 3. If diff > MaxProfit, MaxProfit = Diff
        # 4. Return MaxProfit
        return maxProfit
        