# @leet start
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()
        for i in range(n):
            found = 0
            stored = None

            for j in range(m):
                if grid[i][j] == 1:
                    if found == 0:
                        stored = (i, j)
                    elif found == 1:
                        visited.add(stored)
                        visited.add((i, j))
                    else:
                        visited.add((i, j))
                    found += 1

        for j in range(m):
            found = 0
            stored = None
            for i in range(n):
                if grid[i][j] == 1:
                    if found == 0:
                        stored = (i, j)
                    elif found == 1:
                        visited.add(stored)
                        visited.add((i, j))
                    else:
                        visited.add((i, j))
                    found += 1


        return len(visited)

        
# @leet end
