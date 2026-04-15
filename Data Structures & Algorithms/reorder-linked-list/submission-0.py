# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, arr2 = None, slow.next
        while arr2:
            temp = arr2.next
            arr2.next = prev
            prev = arr2
            if not temp:
                break
            arr2 = temp
        slow.next = None
        
        arr1 = head
        while arr1 and arr2:
            temp1 = arr1.next
            arr1.next = arr2
            arr1 = temp1

            temp2 = arr2.next
            arr2.next = arr1
            arr2 = temp2


        