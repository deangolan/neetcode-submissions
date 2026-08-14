class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])

        memo = [0] * M
        memo[0] = 1

        for i in range(N):
            if obstacleGrid[i][0] == 1:
                memo[0] = 0
            for j in range(1, M): # This doesn't work if the first cell is blocked
                if obstacleGrid[i][j] == 1:
                    memo[j] = 0
                else:
                    memo[j] = memo[j] + memo[j-1]

        return memo[-1]