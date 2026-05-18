class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
            
        edgeMap = {}
        visited = set()
        for n1, n2 in edges:
            visited.add(n1)
            visited.add(n2)
            edgeMap.setdefault(n1, []).append(n2)
            edgeMap.setdefault(n2, []).append(n1)

        path = set()
        def dfs(node, parent):
            if node in path:
                return False
            path.add(node)
            visited.remove(node)
            for n in edgeMap[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True
        
        node, _ = edges[0]
        return dfs(node, None) and len(visited) == 0
