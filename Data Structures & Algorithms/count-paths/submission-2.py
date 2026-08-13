class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for i in range(1, n):
                dp[i] = dp[i] + dp[i-1]

        return dp[-1]