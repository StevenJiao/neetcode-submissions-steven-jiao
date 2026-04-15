# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        newHead = dummy
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            c = 0
            if s >= 10:
                c = 1
                s -= 10
            n = ListNode(s)
            newHead.next = n
            newHead = newHead.next
            l1 = l1.next
            l2 = l2.next
        left = l1 or l2
        while left:
            s = left.val + c
            c = 0
            if s >= 10:
                c = 1
                s -= 10
            n = ListNode(s)
            newHead.next = n
            newHead = newHead.next
            left = left.next
        if c == 1:
            newHead.next = ListNode(1)
        return dummy.next
