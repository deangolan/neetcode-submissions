class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])

        memo = [ [0] * M for _ in range(N) ]
        memo[N-1][M-1] = 1
        
        def traverse(i, j): 
            if i >= N or j >= M:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if memo[i][j] != 0:
                return memo[i][j]
            ans = traverse(i+1, j) + traverse(i, j+1)
            memo[i][j] = ans
            return ans

        return traverse(0, 0)