class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        nodesLeft = set(i for i in range(n))
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node not in nodesLeft:
                return
            nodesLeft.remove(node)
            for nei in adj[node]:
                dfs(nei)

        for i in range(n):
            if i in nodesLeft:
                dfs(i)
                ans += 1
        
        return ans