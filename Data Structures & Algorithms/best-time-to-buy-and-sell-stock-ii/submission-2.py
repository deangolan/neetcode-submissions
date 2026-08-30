class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = 0
        for p in prices:
            if p < sell:
                profit += sell - buy
                buy, sell = p, p
            elif p > sell:
                sell = p
            elif p < buy:
                buy = p
        profit += sell - buy

        return profit