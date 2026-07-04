class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        maxArea = 0
        
        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == 0:
                return
            curArea[0] += 1
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    curArea = [0]
                    dfs(i, j)
                    maxArea = max(maxArea, curArea[0])
        
        return maxArea