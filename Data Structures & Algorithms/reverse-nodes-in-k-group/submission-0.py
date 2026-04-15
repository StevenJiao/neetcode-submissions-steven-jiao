# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        dummy = ListNode(-1, head)
        l = dummy
        r = head
        while r:
            if count < k:
                r = r.next
                count += 1
                continue
            count = 1
            rNext = r.next
            lPrev = l
            newTail = lPrev.next
            newHead = r
            print(f"reversing {newTail.val} to {newHead.val}")
            self.reverse(newTail, newHead)
            print(f"connecting new tail {newTail.val} to {rNext.val if rNext else None}")
            newTail.next = rNext
            print(f"connecting left prev {lPrev.val} to new head {newHead.val} ")
            lPrev.next = newHead
            l = newTail
            r = rNext
        return dummy.next
    
    def reverse(self, l: Optional[ListNode], r: Optional[ListNode]):
        prev = l
        curr = l.next
        after = r.next
        while prev != r:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

