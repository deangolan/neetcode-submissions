class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1, 3, 10], 12
        memo = { 0: 0 }

        def dp(amount):
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            res = min(dp(amount - coin) for coin in coins) + 1
            memo[amount] = res
            return res

        out = dp(amount)
        return out if out != float('inf') else -1

        
