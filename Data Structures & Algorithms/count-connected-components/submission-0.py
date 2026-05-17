class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        comp = 0

        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            seen.add(node)
            # print("added", node)
            for n in adj[node]:
                if n not in seen:
                    dfs(n)

        for node in range(n):
            if node not in seen:
                # print("dfs on", node)
                dfs(node)
                comp += 1

        return comp