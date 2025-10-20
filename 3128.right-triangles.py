# @leet imports start
from typing import *

# @leet imports end
from collections import Counter


# @leet start
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid)
        rows = Counter()
        cols = Counter()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += (rows[i] - 1) * (cols[j] - 1)
        return ans


# @leet end

grid = [[0, 1, 0], [0, 1, 1], [0, 1, 0]]
x = Solution().numberOfRightTriangles(grid)
print(x)

