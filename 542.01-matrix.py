# @leet start
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        nrows = len(mat)
        ncols = len(mat[0])
        for r, row in enumerate(mat):
            for c, ele in enumerate(row):
                if ele == 0:
                    queue.append((r, c))

        # ms-bfs
        visited = set()
        dist = -1

        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                mat[r][c] = dist

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    rn = r + dr
                    cn = c + dc

                    if 0 <= rn < nrows and 0 <= cn < ncols:
                        queue.append((rn, cn))

        return mat


# @leet end


m0 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
e0 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
m1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
e1 = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
x = Solution().updateMatrix(m1)
print(x)
print(x == e1)
