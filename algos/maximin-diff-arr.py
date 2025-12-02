# @leet imports start
from typing import List

# @leet imports end


# TODO: redo!

# Leetcode 2528
# this question tests a lot of things
# maximin or minimax usually means bsearch
# radius may be sweep line or merging intervals


# @leet start
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # build k additional stations, each with radius r
        # get the minimum power station of all cities
        # maximise the weakest link

        def is_achievable(x: int, sweeps: List[int]) -> bool:
            # return True if this minimum power x is achievable

            # if we spam in the weakest link, and x is too high,
            # then we want to decrease x
            # O(n) time complexity here
            sweeps = sweeps[:]
            remaining = k
            curr = 0

            for i in range(n):
                curr += sweeps[i]
                if curr < x:
                    diff = x - curr
                    if diff > remaining:
                        return False
                    remaining -= diff
                    curr += diff
                    # NOTE: at city i, build at i + r. So the end is i + 2 * r + 1
                    sweeps[min(n, i + 2 * r + 1)] -= diff

            return True

        n = len(stations)
        diffs = [0] * (n + 1)
        for i in range(n):
            diffs[max(0, i - r)] += stations[i]
            diffs[min(i + r + 1, n)] -= stations[i]

        # r caps at n-1, i.e. every station affects every other station
        # n <= 10**5
        # k <= 10**9
        # so max power is sum of all stations + k
        # so actually, you dont need to calculate the power each city has

        lo = min(stations)
        hi = sum(stations) + k + 1  # exclusive hi
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if is_achievable(mid, diffs):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1


# @leet end

s = [1, 2, 4, 5, 0]
r = 1
k = 2
x = Solution().maxPower(s, r, k)
print(x)

s = [4, 4, 4, 4]
r = 0
k = 3
x = Solution().maxPower(s, r, k)
print(x)
