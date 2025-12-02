# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
# NOTE: same as 1024. Video Stitching
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # furthest reach from each start point
        maxR = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            L, R = (max(0, i - r), min(i + r, n))
            maxR[L] = max(maxR[L], R)

        covered = 0  # the globally max covered point
        frontier = 0  # how far you can expand the frontier
        ans = 0

        # i is the current point to cover
        for i in range(n):
            frontier = max(frontier, maxR[i])

            if i == frontier:  # cannot expand frontier further than here
                return -1

            # the current point cannot be covered by previous taps,
            # need to use another tap
            if i == covered:
                ans += 1
                covered = frontier

        return ans


# @leet end


class SolutionSort:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        covers = []
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            item = (max(0, i - r), min(i + r, n))
            covers.append(item)
        covers.sort()

        covered = 0
        i = 0
        frontier = 0  # how far you can expand the frontier
        ans = 0

        while covered < n:
            while i < len(covers) and covers[i][0] <= covered:
                frontier = max(frontier, covers[i][1])
                i += 1

            # frontier cannot expand any further
            if frontier == covered:
                return -1

            covered = frontier
            ans += 1

        return ans


class SolutionWrong:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        covers = []
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            item = (max(0, i - r), min(i + r, n))
            covers.append(item)

        covers.sort(key=lambda x: (x[0], -x[1]))

        to_cover = 0
        ans = 0
        i = 0
        m = len(covers)
        print(covers)
        while i < m:
            ans += 1
            s, e = covers[i]
            # (0, 5), ignore (0, 3)
            # if to_cover > e:
            #     continue

            if s > to_cover:
                return -1

            # (0,5), (0,3), (2,6), (3,9)
            #   ^      x      x      ^
            j = i + 1
            while j < m and covers[j][0] <= e:
                # in the following, take the largest cover
                to_cover = max(to_cover, covers[j][1])
                j += 1
            if to_cover > e:
                ans += 1

            i = j

        if to_cover < n:
            return -1

        return ans if ans > 0 else -1


x = ""
n = 5
r = [3, 4, 1, 1, 0, 0]
# x = Solution().minTaps(n, r)
print(x)

n = 7
r = [1, 2, 1, 0, 2, 1, 0, 1]
x = Solution().minTaps(n, r)
print(x)
