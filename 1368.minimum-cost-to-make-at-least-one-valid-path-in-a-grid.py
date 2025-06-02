from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# @leet start
class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        # The key point is that this is actually a graph question...
        # TC: O(V + E logV) = O(nlogn)
        # SC: O(n) for pq, dists
        # apparently using a deque in 0-1 bfs is more efficient

        n = len(grid)
        m = len(grid[0])

        dirs = {
            1: (0, 1),  # right
            2: (0, -1),  # left
            3: (1, 0),  # down
            4: (-1, 0),  # up
        }

        # construct a weighted graph with correct dir weight 0 and wrong dir weight 1
        graph = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            for j in range(m):
                for dir, (di, dj) in dirs.items():
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < n and 0 <= nj < m:
                        graph[(i, j)][(ni, nj)] = 0 if dir == grid[i][j] else 1

        # dijkstra
        root = (0,0)
        pq = [root]
        dists = defaultdict(lambda: n * m)
        dists[root] = 0
        while pq:
            curr = heappop(pq)
            if curr == (n - 1, m - 1):
                return dists[(n - 1, m - 1)]

            nbs = graph[curr].items()
            for nb, weight in nbs:
                if dists[curr] + weight < dists[nb]:
                    dists[nb] = dists[curr] + weight
                    heappush(pq, nb)

        return -1


# @leet end

grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
x = Solution().minCost(grid)
print(x)

