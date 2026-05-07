class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        r = 1
        while r < len(prices): 
            while prices[r] - prices[l] < 0 and l < r:
                l += 1

            profit = max(profit, prices[r] - prices[l])
            
            r += 1

        return profit