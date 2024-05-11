// https://leetcode.com/problems/k-closest-points-to-origin

from heapq import heapify, heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # heap will store values of (dist, p)
        # heapify(heap) # you dont need to heapify an empty list cos it is alr a heap

        n = len(points)

        def sq(x) -> int:
            return x ** 2

        for p in points:
            dist_sq = sq(p[0]) + sq(p[1])
            heappush(heap, (-dist_sq, p)) 
            #add tuple to the heap, but instead using dist_sq which is alw positive
            # so -dist_sq makes a maxheap instead, 
            # and the smallest elements remain in the heap

            if len(heap) > k:
                # get rid of the largest elements
                heappop(heap)

        ans = []
        for t in heap:
            ans.append(t[1])

        return ans




