class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1. Set initial values. MaxProfit = 0
        maxProfit = 0
        lCtr, rCtr = 0, 1

        # Loop through list. Increment lCtr if a low number is found. If not, increment rCtr
        while rCtr < len(prices):
            # If value on right is greater, find profit and maxProft
            if prices[lCtr] < prices[rCtr]:
                profit = prices[rCtr] - prices[lCtr]
                maxProfit = max(profit, maxProfit)
            else:
                # If value on right is lesser, it should become the next lowest value
                lCtr = rCtr

            rCtr +=1

        return maxProfit


                




        
        # 3. If diff > MaxProfit, MaxProfit = Diff
        # 4. Return MaxProfit
        return maxProfit
        