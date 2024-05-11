// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:
    from heapq import heapify, heappush, heappop

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapify(self.heap)
        for i in nums:
            heappush(self.heap, i)
        while len(self.heap) > self.k:
                heappop(self.heap)
            

             

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)