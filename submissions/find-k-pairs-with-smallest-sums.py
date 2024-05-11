// https://leetcode.com/problems/find-k-pairs-with-smallest-sums

# with the cartesian product, find the minimum pairs

from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
                # note that at this pt the prev accounted pair is still in the 

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1
        
        return ans