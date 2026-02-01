# A heap is a complete binary tree
# where the parent key <= child keys

# 0-based indexing:
# The parent is stored at index (k - 1) // 2
# The left child is stored at index 2k + 1
# The right child is stored at index 2k + 2

from typing import Any, Protocol, Self, runtime_checkable


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, value: Any, /) -> bool: ...


class Heap[T: Comparable]:
    # Min-Heap implementation
    def __init__(self):
        self.heap = []

    def __repr__(self) -> str:
        return f"Heap({self.heap})"

    @classmethod
    def heapify(cls, nums: list[T]) -> Self:
        n = len(nums)
        heap = cls()
        heap.heap = nums[:]
        for i in range(n // 2 - 1, -1, -1):
            heap._sift_down(i)
        return heap

    def peek(self) -> T:
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, val: T):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self) -> T:
        if len(self.heap) == 0:
            raise IndexError("Empty heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, i: int) -> None:
        # Compare node with parent, and swap if node is smaller
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    # Swap elements at indices i and j
    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_down(self, i: int) -> None:
        # Find the smallest among i, left, right
        # Swap i with smallest and continue sifting down

        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest


if __name__ == "__main__":
    h = Heap[int]()
    h.insert(3)
    h.insert(1)
    h.insert(4)
    h.insert(2)
    h.insert(8)
    h.insert(6)
    h.insert(5)
    h.insert(0)
    h.insert(9)

    print(h)

    while not h.is_empty():
        print(h.extract_min())
