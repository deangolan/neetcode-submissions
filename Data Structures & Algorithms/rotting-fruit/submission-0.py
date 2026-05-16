class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        fresh = 0
        queue = deque([])
        for i, row in enumerate(grid):
            for j, fruit in enumerate(row): 
                if fruit == 1:
                    fresh += 1
                elif fruit == 2:
                    queue.append((i, j))
        
        # bfs
        time = 0 
        while queue and fresh > 0:
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                    if 0 <= ni < ROW and 0 <= nj < COL and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))
            time += 1

        return time if fresh == 0 else -1