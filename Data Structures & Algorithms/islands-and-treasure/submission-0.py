class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        INF = 2147483647

        queue = deque([])
        visited = set()
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0:
                    queue.append((i, j, 0))
        
        while queue:
            n = len(queue)
            for _ in range(n):
                i, j, distance = queue.popleft()
                if i >= 0 and i < ROW and j >= 0 and j < COL \
                    and grid[i][j] != -1 and (i, j) not in visited:
                    if distance > 0:
                        grid[i][j] = distance
                    distance += 1
                    queue.append((i+1, j, distance))
                    queue.append((i-1, j, distance))
                    queue.append((i, j+1, distance))
                    queue.append((i, j-1, distance))

                visited.add((i, j))

