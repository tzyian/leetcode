# @leet start
from heapq import heappush, heappushpop


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        # minheap
        heap = []

        for kid in happiness:
            if len(heap) > k:
                heappushpop(heap, kid)
            else:
                heappush(heap, kid)

        heap.sort(reverse=True)
        total = 0
        for i in range(k):
            if heap[i] > i:
                total += heap[i] - i
            else:
                break

        return total


# @leet end
