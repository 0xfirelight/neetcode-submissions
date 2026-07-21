# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 

        current = head.next
        prev = head

        while current:
            tmp_next = current.next
            # point current node to the previous node
            current.next = prev

            # store previous node
            if prev == head:
                prev.next = None
                
            prev = current

            # move the pointer to the next node
            current = tmp_next

        return prev

        