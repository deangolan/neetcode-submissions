class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = { i: [] for i in range(n) }
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(node, nei):
                    return False
            
            return True

        return dfs(None, 0) and len(visited) == n