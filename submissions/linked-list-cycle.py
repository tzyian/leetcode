// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        if p1 is None:
            return False
        p2 = head.next
        
        while p1 != p2:    
            if p1 is None or p2 is None or p2.next is None:
                return False
            p2 = p2.next.next
            p1 = p1.next
        return True
            


        