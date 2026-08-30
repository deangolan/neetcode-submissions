class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        for i, p in enumerate(prices):
            if p < prices[sell]:
                profit += prices[sell] - prices[buy]
                buy, sell = i, i
            elif p > prices[sell]:
                sell = i
            elif p < prices[buy]:
                buy = i
        profit += prices[sell] - prices[buy]

        return profit