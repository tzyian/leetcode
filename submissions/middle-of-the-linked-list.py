// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        if not head.next:
            return head

        slow = head
        fast = head
        while slow and fast and slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
