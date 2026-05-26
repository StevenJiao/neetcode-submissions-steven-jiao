"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        head = Node(node.val)
        currCpy = head
        oldToNew = {node: currCpy}
        q = deque([node])
        while q:
            currNode = q.popleft()
            currCpy = oldToNew.get(currNode, Node(currNode.val))
            for child in currNode.neighbors:
                if child not in oldToNew:
                    q.append(child)
                    oldToNew[child] = Node(child.val)
                currCpy.neighbors.append(oldToNew[child])

        return head