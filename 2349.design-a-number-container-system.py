# @leet start
from collections import defaultdict
from heapq import heappop, heappush

Heap = list[int]


class NumberContainers:
    # lazy version of the C++ version, which only changes ordering on find
    # SC O(n)

    def __init__(self):
        # reminder that python heaps are by default minheap
        self.num_to_heap: defaultdict[int, Heap] = defaultdict(list)
        self.containers: dict[int, int] = dict()

    def change(self, index: int, number: int) -> None:
        self.containers[index] = number
        heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        # TC amortised O(logn) of 1 find operation over k change operations
        while self.num_to_heap[number]:
            cont = self.num_to_heap[number][0]
            if self.containers[cont] == number:
                return cont
            heappop(self.num_to_heap[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @leet end
