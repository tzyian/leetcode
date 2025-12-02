# @leet imports start
from typing import List, Optional

# @leet imports end

from collections import defaultdict
from heapq import heappush, heappop, heapify


# @leet start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**10
        graph = defaultdict(dict)

        for i, (x, y) in enumerate(points):
            for j, (a, b) in enumerate(points):
                graph[i][j] = abs(x - a) + abs(y - b)
                graph[j][i] = abs(x - a) + abs(y - b)

        visited = [False] * n  # alr in MST

        cheapest = [inf] * n  # cheapest edge to get from i to MST
        cheapest[0] = 0

        parent = [-1] * n

        heap = [(0, 0)]

        total_wt = 0

        while heap:
            w, u = heappop(heap)
            if visited[u]:
                continue

            total_wt += w
            visited[u] = True

            for nb, nw in graph[u].items():
                if not visited[nb] and nw < cheapest[nb]:
                    cheapest[nb] = nw
                    parent[nb] = u
                    heappush(heap, (nw, nb))

        return total_wt


# @leet end

p = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
x = Solution().minCostConnectPoints(p)
print(x)

