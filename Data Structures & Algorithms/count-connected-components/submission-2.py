class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        neighbors = {}
        for v1, v2 in edges:
            neighbors.setdefault(v1, []).append(v2)
            neighbors.setdefault(v2, []).append(v1)

        visited = set()
        def dfs(v):
            if v in visited:
                return 0

            visited.add(v)
            for n in neighbors.get(v, []):
                dfs(n)

            return 1

        for v in range(n):
            count += dfs(v)

        return count