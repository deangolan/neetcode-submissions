class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0] * n for _ in range(m) ]
        def walk(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != 0:
                return dp[i][j]
            paths = walk(i+1, j) + walk(i, j+1)
            dp[i][j] = paths 
            return paths
        return walk(0, 0)