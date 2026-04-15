# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = None, head
        count = 0
        while second:
            second = second.next
            if count == n:
                first = first.next if first else head
            else:
                count += 1 
        print(first.val if first else first, second.val if second else second)
        if not first:
            head = head.next
        else:
            first.next = first.next.next if first.next else None
        return head
        