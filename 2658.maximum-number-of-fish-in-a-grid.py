# @leet start
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [-1, 0, 1, 0, -1]

        maxfish = 0

        def invalid(i: int, j: int) -> bool:
            return i < 0 or i > n - 1 or j < 0 or j > m - 1

        def dfs(i: int, j: int) -> int:
            stack = [(i, j)]
            tot = 0
            while stack:
                ci, cj = stack.pop()
                if invalid(ci, cj) or grid[ci][cj] == 0:
                    continue

                tot += grid[ci][cj]
                grid[ci][cj] = 0

                for k in range(1, len(dirs)):
                    stack.append((ci + dirs[k - 1], cj + dirs[k]))

            return tot

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                pool = dfs(i, j)
                maxfish = max(maxfish, pool)

        return maxfish

        
# @leet end
