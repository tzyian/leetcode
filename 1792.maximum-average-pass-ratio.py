from heapq import heapify, heapreplace
from typing import List


# @leet start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # goal is to find the maximum sum of ratios
        n = len(classes)

        # O(n) heapify
        heap = []
        for npasses, ntot in classes:
            diff = (npasses + 1) / (ntot + 1) - (npasses / ntot)
            # diff is -ve for maxheap
            heap.append((-diff, npasses, ntot))
        heapify(heap)

        # k * logn pushpops
        for _ in range(extraStudents):
            _, nstuds, ntot = heap[0]
            new_passes = nstuds + 1
            new_tot = ntot + 1
            newdiff = (new_passes + 1) / (new_tot + 1) - new_passes / new_tot
            heapreplace(heap, (-newdiff, new_passes, new_tot))

        tot = sum([a / b for _, a, b in heap])

        return tot / n


# @leet end
