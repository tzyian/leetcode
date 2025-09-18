from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @leet start
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # count == number of nodes seen so far
        # while stream:
        # reservoir[i] = newnode.data where randint(0, count) == i if i <= k

        curr = self.head
        reservoir = int(10e5)
        count = 0
        while curr:
            rep = randint(0, count)
            if rep == 0:
                reservoir = curr.val
            curr = curr.next
            count += 1
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @leet end

