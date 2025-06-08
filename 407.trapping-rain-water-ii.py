from heapq import heappop, heappush
from typing import List


# @leet start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # NOTE: to redo lol
        # bfs + minheap
        # TC = O(nm log(nm)), where log(nm) is heap-ops
        # SC = O(nm)

        # my first instinct is to do 1d trapping rain water across every row
        # to fill up a grid of potential values
        # then do 1d trapping rain water across every col
        # then min across the two

        # note that this will fail for example 2
        # where the 1d scan will think the centre fills 1 rather than 2

        # [[3, 3, 3, 3, 3],
        #  [3, 2, 2, 2, 3],
        #  [3, 2, 1, 2, 3],
        #  [3, 2, 2, 2, 3],
        #  [3, 3, 3, 3, 3]]

        n = len(heightMap)
        m = len(heightMap[0])

        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < m

        # the ans is apparently to use bfs + minheap
        # add the perimeter to the pq, pop and maintain the max height

        visited = [[False] * m for _ in range(n)]

        heap = []
        for i in range(n):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][m - 1], i, m - 1))
            visited[i][0] = True
            visited[i][m - 1] = True
        for j in range(m):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[n - 1][j], n - 1, j))
            visited[0][j] = True
            visited[n - 1][j] = True

        total = 0
        maxht = 0

        while heap:
            ht, r, c = heappop(heap)
            maxht = max(ht, maxht)
            dirs = [0, 1, 0, -1, 0]
            for i in range(1, len(dirs)):
                dr, dc = dirs[i], dirs[i - 1]
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and not visited[nr][nc]:
                    heappush(heap, (heightMap[nr][nc], nr, nc))
                    """
                    NOTE: this is the trippy part. The intuition is that 
                    by using a minheap, the maxht will almost always == last_popped
                    But if there are neighbours which fill water, last_popped < maxht
                    e.g. you pop 3, and add 1 to neighbour, which can fill 3-1=2.
                    Likewise next_popped = 0, fills 3-0 = 3
                    The boundaries 9 and 6 are in the heap. so maxht 3 is the boundary.

                    5 9 6 6
                    3 1 0 6
                    5 5 9 6

                    5 5 5 5
                    3 2 2 5
                    3 0 2 5
                    3 3 3 5

                    All 5s and the perimeter 3 are in the boundary. 
                    Height is 5 here.

                    5 5 2 5
                    3 2 2 5
                    3 0 2 5
                    3 3 3 5

                    All the 2s and 0 are popped before 3 is even popped.

                    """

                    total += max(0, maxht - heightMap[nr][nc])
                    visited[nr][nc] = True

        return total


# @leet end
