from collections import deque
from typing import List


# @leet start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # NOTE: this fails on the last test case below where
        # y is 2 from A, 3 from B. x is 3 from A, 2 from B. But x < y and y is visited first.
        # See the cpp solution

        # edges is a list of index to target
        # ms-bfs

        # case when both nodes are the same
        if node1 == node2:
            return node1

        n1_visited = set([-1, node1])
        n2_visited = set([-1, node2])

        curr1 = node1
        curr2 = node2

        for _ in range(len(edges)):

            if curr1 == curr2:
                return curr1
            n1_visited.add(curr1)
            n2_visited.add(curr2)

            if curr1 in n2_visited:
                return curr1
            elif curr2 in n1_visited:
                return curr2

            n1_next = edges[curr1]
            n2_next = edges[curr2]
            if n1_next in n1_visited:
                n1_next = curr1
            if n2_next in n2_visited:
                n2_next = curr2

            curr1 = n1_next
            curr2 = n2_next

        return -1

        
# @leet end

# edges = [2, 2, 3, -1]
# n1 = 0
# n2 = 1
# x = Solution().closestMeetingNode(edges, n1, n2)
# print(x)  # expected 2
#
#
# e2 = [1, 2, -1]
# n1 = 0
# n2 = 2
# x = Solution().closestMeetingNode(e2, n1, n2)
# print(x)  # expected 2
#
#
# e3 = [4,4,4,5,1,2,2]
# n1 = 1
# n2 = 1 # expected 1

e4 = [4, 4, 8, -1, 9, 8, 4, 4, 1, 1]
n1 = 5
n2 = 6
x = Solution().closestMeetingNode(e4, n1, n2)
# print(x)  # expected 1

