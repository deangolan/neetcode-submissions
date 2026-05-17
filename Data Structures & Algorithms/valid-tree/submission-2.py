class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = [[] for _ in range(n)]
        needed = set()
        for n1, n2 in edges:
            needed.add(n1)
            needed.add(n2)
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        seen = set()

        def dfs(parent, node): 
            if node in seen:
                return False
            seen.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(node, n):
                    return False
            return True

        return dfs(None, edges[0][0]) and seen == needed