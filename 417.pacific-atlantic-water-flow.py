from collections import deque
from typing import List

# @leet start
coord = tuple[int, int]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ms-bfs from the 2 corners
        n = len(heights)
        m = len(heights[0])

        dirs = [0, 1, 0, -1, 0]

        def is_valid(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        pacq = [(0, i) for i in range(m)] + [(i, 0) for i in range(n)]
        atlq = [(n - 1, i) for i in range(m)] + [(i, m - 1) for i in range(n)]

        reachable = [[[False, False] for _ in range(m)] for _ in range(n)]

        def dfs(stack: list[coord], ind: int):
            visited = [[False] * m for _ in range(n)]
            for i, j in stack:
                visited[i][j] = True
                reachable[i][j][ind] = True

            while stack:
                i, j = stack.pop()

                for d in range(1, len(dirs)):
                    di, dj = dirs[d], dirs[d - 1]
                    ni, nj = i + di, j + dj

                    if (
                        is_valid(ni, nj)
                        and heights[ni][nj] >= heights[i][j]
                    ):
                        reachable[ni][nj][ind] = True

                        if not visited[ni][nj]:
                            stack.append((ni, nj))
                            visited[ni][nj] = True

        dfs(pacq, 0)
        dfs(atlq, 1)

        ans = []
        for i in range(n):
            for j in range(m):
                if reachable[i][j][0] and reachable[i][j][1]:
                    ans.append([i, j])
        return ans


# @leet end

l = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
l = [[2,1],[1,2]]
x = Solution().pacificAtlantic(l)
print(x)

