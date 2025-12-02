# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def minRectanglesToCoverPoints(
        self,
        points: List[List[int]],
        w: int,
    ) -> int:
        pts = sorted(list(set(x for (x, _) in points)))
        ans = 0
        rect_end = -1
        for pt in pts:
            if rect_end < pt:
                ans += 1
                rect_end = pt + w

        return ans

    def minRectanglesToCoverPointsSlow(self, points: List[List[int]], w: int) -> int:
        pts = list(set(x for (x, _) in points))
        pts.sort()
        ans = 0

        x = pts[0]
        i = 0
        n = len(pts)
        while x <= pts[-1] and i < n:
            ans += 1
            x += w + 1

            while i < n and pts[i] < x:
                i += 1
            if i < n and x < pts[i]:
                x = pts[i]

        return ans


# @leet end

p = [[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]]
w = 1
x = Solution().minRectanglesToCoverPoints(p, w)
print(x)

[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
2

[[2, 3], [1, 2]]
0

