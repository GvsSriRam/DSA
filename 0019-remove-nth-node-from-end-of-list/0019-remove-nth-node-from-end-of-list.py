# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for _ in range(n):
            end = end.next
        
        if not end:
            return head.next
        
        to_remove = head
        prev = head
        while end:
            prev = to_remove
            to_remove = to_remove.next
            end = end.next
        prev.next = to_remove.next
        
        return head