class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        memo = [0] * M
        for j in range(1, M):
            memo[j] = float('inf') 

        for i in range(N):
            for j in range(M):
                if j > 0:
                    memo[j] = grid[i][j] + min(memo[j-1], memo[j])
                else:
                    memo[j] = grid[i][j] + memo[j]

        return memo[-1]