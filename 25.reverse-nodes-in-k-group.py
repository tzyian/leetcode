# @leet imports start
from typing import List, Optional, Tuple

# @leet imports end


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # stop is the node AFTER the group we reverse
        def reverseLL(
            head: Optional[ListNode], stop: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not head:
                return head

            prev = None
            curr = head

            while curr and curr != stop:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        if not head or k == 1:
            return head

        sentinel = ListNode(-1)
        sentinel.next = head

        curr = head
        prev = sentinel
        to_be_tail = curr

        while curr:
            grp_size = 0
            while curr and grp_size < k:
                curr = curr.next
                grp_size += 1

            if prev and prev.next and grp_size == k:
                to_be_tail = prev.next
                prev.next = reverseLL(prev.next, curr)
                to_be_tail.next = curr

            prev = to_be_tail

        return sentinel.next


# @leet end

