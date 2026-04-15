"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}
        dummy = Node(0)
        copyHead = dummy
        curr = head
        while curr:
            newNode = seen[curr] if curr in seen else Node(curr.val)
            if curr not in seen:
                seen[curr] = newNode

            newNode.next = seen[curr.next] if curr.next in seen else Node(curr.next.val)
            if curr.next not in seen:
                seen[curr.next] = newNode.next
            
            newNode.random = seen[curr.random] if curr.random in seen else Node(curr.random.val)
            if curr.random not in seen:
                seen[curr.random] = newNode.random

            # copyHead = copyHead.next
            curr = curr.next
        return seen[head]