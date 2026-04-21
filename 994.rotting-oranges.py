# @leet imports start
from collections import deque
from typing import List

# @leet imports end


# @leet start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        starts = []
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        oranges_left = 0
        for i in range(n):
            for j in range(m):
                match grid[i][j]:
                    case 1:
                        oranges_left += 1
                    case 2:
                        starts.append((i, j))

        dq = deque(starts)
        time = 0
        visited = set(starts)
        while dq:
            if oranges_left == 0:
                return time

            count = len(dq)
            for i in range(count):
                ci, cj = dq.popleft()
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if (
                        not 0 <= ni < n
                        or not 0 <= nj < m
                        or (ni, nj) in visited
                        or grid[ni][nj] == 0
                    ):
                        continue
                    if grid[ni][nj] == 1:
                        oranges_left -= 1
                        visited.add((ni, nj))
                        dq.append((ni, nj))
            time += 1

        return time if oranges_left == 0 else -1


# @leet end

