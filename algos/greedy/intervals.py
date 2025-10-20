from typing import List

"""
Given a list of ranges, find the minimum number of ranges
that can cover the entire interval [0, n]
(inclusive, allow overlaps)
"""


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
