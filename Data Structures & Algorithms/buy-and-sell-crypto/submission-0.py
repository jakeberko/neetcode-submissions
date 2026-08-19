class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        if len(prices) == 1:
            return 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                profit = max(curr_profit, profit)
            else:    
                l = r
            r += 1      
        
        return profit