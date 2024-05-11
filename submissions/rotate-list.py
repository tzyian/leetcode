// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# find length
# mod k to find number of times to rotate
# connect the last element to the head
# break the list at the partition

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        # edge cases
        if not head:
            return
        elif not head.next:
            return head
        
        # find length
        len = 1
        last = head
        while last.next:
            len += 1
            last = last.next

        # find absolute rotation
        k %= len

        # short circuit if no rotation needed
        if k == 0:
            return head

        # connect last element 
        last.next = head

        # find the breakpoint
        node = last
        bp = len - k
        while bp:
            bp -= 1
            node = node.next

        temp = node.next
        node.next = None

        return temp



        

        