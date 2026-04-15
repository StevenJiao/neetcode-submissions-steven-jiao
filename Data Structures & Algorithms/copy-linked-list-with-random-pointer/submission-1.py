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
        dummy = Node(-1)
        copyHead = dummy
        while head:
            newNode = seen[head] if head in seen else Node(head.val)
            if head not in seen:
                seen[head] = newNode

            copyHead.next = newNode
            if head.random not in seen:
                seen[head.random] = Node(head.random.val)
                newNode.random = seen[head.random]
            else:
                newNode.random = seen[head.random]

            copyHead = copyHead.next
            head = head.next
        return dummy.next