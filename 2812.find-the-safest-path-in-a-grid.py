# @leet imports start
from collections import deque
from heapq import heapify, heappop, heappush
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid)
        m = len(grid[0])

        def in_graph(i, j) -> bool:
            return 0 <= i < n and 0 <= j < m

        # ms-bfs
        safeness = [[-1] * m for _ in range(n)]
        que = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    safeness[i][j] = 0
                    que.append((i, j))

        while que:
            i, j = que.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not in_graph(ni, nj) or safeness[ni][nj] != -1:
                    continue
                que.append((ni, nj))
                safeness[ni][nj] = safeness[i][j] + 1

        # minimax dijkstra
        pq = [(-safeness[0][0], 0, 0)]
        best = [[-1] * m for _ in range(n)]
        best[0][0] = safeness[0][0]
        while pq:
            curr, i, j = heappop(pq)
            curr = -curr
            if i == n - 1 and j == m - 1:
                return curr
            if curr < best[i][j]:
                continue
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not in_graph(ni, nj):
                    continue
                ncurr = min(curr, safeness[ni][nj])
                if ncurr > best[ni][nj]:
                    best[ni][nj] = ncurr
                    heappush(pq, (-ncurr, ni, nj))
        return -1


# @leet end

