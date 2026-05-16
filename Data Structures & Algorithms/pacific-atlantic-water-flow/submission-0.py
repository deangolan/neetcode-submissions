class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        
        pacificReach = set()
        atlanticReach = set()

        def dfs(i, j, prev, ocean):
            if i < 0 or i >= ROW or j < 0 or j >= COL or heights[i][j] < prev:
                return
            if ocean == 'Pacific':
                if (i, j) in pacificReach:
                    return
                pacificReach.add((i, j))
            elif ocean == 'Atlantic':
                if (i, j) in atlanticReach:
                    return
                atlanticReach.add((i, j))
            h = heights[i][j]
            dfs(i+1, j, h, ocean)
            dfs(i-1, j, h, ocean)
            dfs(i, j+1, h, ocean)
            dfs(i, j-1, h, ocean)
        
        for i in range(ROW):
            dfs(i, 0, 0, 'Pacific')
            dfs(i, COL-1, 0, 'Atlantic')

        for j in range(COL):
            dfs(0, j, 0, 'Pacific')
            dfs(ROW-1, j, 0, 'Atlantic')
        
        return [[i, j] for i, j in pacificReach.intersection(atlanticReach)]

        