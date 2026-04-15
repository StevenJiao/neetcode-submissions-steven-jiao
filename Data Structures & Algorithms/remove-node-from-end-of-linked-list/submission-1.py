# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        first, second = dummyHead, head
        count = 0
        while count < n:
            count += 1
            second = second.next

        while second:
            second = second.next
            first = first.next

        first.next = first.next.next
        return dummyHead.next
        