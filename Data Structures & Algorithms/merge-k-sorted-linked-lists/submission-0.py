# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode()
        curr = dummy
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0) if lists else None
            lists.append(self.merge2Lists(l1, l2))
        return lists[0]

    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            nextNode = None
            if l1 and l2:
                if (l1.val <= l2.val):
                    nextNode = l1
                    l1 = l1.next
                else:
                    nextNode = l2
                    l2 = l2.next
            elif l1:
                nextNode = l1
                l1 = l1.next
            elif l2:
                nextNode = l2
                l2 = l2.next

            if nextNode:
                curr.next = nextNode
                nextNode.next = None
            else:
                break
            curr = curr.next
        return dummy.next
