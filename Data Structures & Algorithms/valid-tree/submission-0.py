class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = {i:[] for i in range(n)}

        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)

        visited = set()
        q = deque([(0,-1)])
        visited.add(0)
        while q:
            node, parent = q.popleft()
            for neighbour in neighbours[node]:
                if neighbour in visited and neighbour != parent:
                    return False
                elif neighbour in visited and neighbour == parent:
                    continue
                visited.add(neighbour)
                q.append((neighbour, node))
        return len(visited) == n