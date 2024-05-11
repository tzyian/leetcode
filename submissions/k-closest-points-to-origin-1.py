// https://leetcode.com/problems/k-closest-points-to-origin

from heapq import heapify, heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # heap will store values of (dist, p)
        # heapify(heap) # you dont need to heapify an empty list cos it is alr a heap

        ans_tuple = []
        n = len(points)

        def sq(x) -> int:
            return x ** 2

        for p in points:
            dist_sq = sq(p[0]) + sq(p[1])
            heappush(heap, (dist_sq, p)) #add tuple to the heap

            if len(heap) >  n - k:
                # add the smallest elements to ans_tuple
                ans_tuple.append(heappop(heap))

        ans = []
        for t in ans_tuple:
            ans.append(t[1])

        return ans




