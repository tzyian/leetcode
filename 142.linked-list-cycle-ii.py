# @leet imports start
from typing import List, Optional

# @leet imports end


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @leet start
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return

        # 2nd iter
        slow = head
        while slow != fast:
            assert slow and fast
            slow = slow.next
            fast = fast.next

        return slow


# @leet end
