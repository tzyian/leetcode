from heapq import heappop, heappush
from typing import List


# @leet start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # line sweep
        # O(n) for heap
        # O(nlogn) for enum * heap-op

        # to redo

        kp = []  # (bldg-start, h, bldg-endpoint)
        for l, r, h in buildings:
            kp.append((l, -h, r))
            kp.append((r, 0, -1))  # append 0s here to get rid of old bldgs
        kp.sort()

        ans = []
        heap = [(0, float("inf"))]  # (h, end). Ground is never popped
        prev_max = 0

        for x, negh, r in kp:
            while heap[0][1] <= x:  # get rid of expired bldgs
                heappop(heap)

            if negh != 0:  # push only bldgs
                heappush(heap, (negh, r))

            curr_max = -heap[0][0]
            if prev_max != curr_max:
                ans.append([x, curr_max])  # (r,0,-1) is included for this here
                prev_max = curr_max

        return ans


# @leet end
b = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
x = Solution().getSkyline(b)
print(x)

