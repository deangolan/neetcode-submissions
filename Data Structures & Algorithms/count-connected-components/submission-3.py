class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

            return 1

        return sum(dfs(node) for node in range(n))