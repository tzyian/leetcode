# @leet imports start
from typing import List, Optional

# @leet imports end


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @leet start
# if a goes to headA and b goes to headB after reaching tail
# they will reach the intersection at the same time
# whether the intersection is None or Node


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# @leet end

