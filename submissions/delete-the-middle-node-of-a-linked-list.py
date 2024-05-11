// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check for empty list
        if not head:
            return head

        if not head.next:
            return None
        
        # initialise the 2 pointers
        slow = head
        fast = head
        prev = head
        
        # iterate
        while slow and slow.next and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

        return head