# @leet start
from heapq import heappush, heappushpop


class MedianFinder:

    # Note: C++ default seems to use max-heap
    # Java PQ is min_heap, use
    #     `PriorityQueue<Integer>(Collections.reverseOrder())`
    #     to avoid overflow issues
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # Python heaps are min heaps by default
        # Always ensure max_heap == min_heap
        # Or min_heap == max_heap + 1

        if len(self.min_heap) == len(self.max_heap):
            pop = heappushpop(self.max_heap, -num)
            # -pop to get back original number
            heappush(self.min_heap, -pop)
        else:  # minheap has 1 more
            pop = heappushpop(self.min_heap, num)
            heappush(self.max_heap, -pop)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            # negate max_heap to get back original number
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:  # minheap has 1 more
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @leet end
