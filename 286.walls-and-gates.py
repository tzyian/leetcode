from typing import List
from collections import deque

INF = 2147483647


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        sources = deque()
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 0:
                    sources.append((i, j))
        if not sources:
            return

        dirs = [1, 0, -1, 0, 1]
        level = 0
        # msbfs
        while sources:
            times = len(sources)
            for _ in range(times):
                i, j = sources.popleft()
                grid[i][j] = level
                for d in range(1, len(dirs)):
                    di, dj = dirs[d], dirs[d - 1]
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                        sources.append((ni, nj))
            level += 1

        return
