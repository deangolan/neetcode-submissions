class Solution:
    def climbStairs(self, n: int) -> int:
        # semiring: (add, )
        # 4 = dp(2)
        # 3 = 1 + 2
        memo = [None] * (n + 3) 
        memo[n] = 1
        memo[n+1] = 0
        memo[n+2] = 0
        for i in range(n-1, -1, -1):
            memo[i] = memo[i+1] + memo[i+2]
        return memo[0]