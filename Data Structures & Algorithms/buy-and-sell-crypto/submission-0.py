class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        r = 1

        while r < len(prices):
            pricel = prices[l]
            pricer = prices[r]
            if pricel >= pricer:
                l = r
                r = l + 1
            else:
                canidate = pricer - pricel
                if canidate > profit:
                    profit = canidate
                r += 1

        return profit