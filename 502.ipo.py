# @leet imports start
from typing import List, Optional

# @leet imports end

from heapq import heappush, heappop, heapify


# @leet start
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        cp = sorted(zip(capital, profits))

        i = 0
        cap = w
        heap = []  # max heap

        for _ in range(k):
            while i < n and cp[i][0] <= cap:
                heappush(heap, -cp[i][1])
                i += 1

            if not heap:
                break
            cap += -heappop(heap)
        return cap


# @leet end

