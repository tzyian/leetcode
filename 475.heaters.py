# @leet imports start
# @leet imports end
from bisect import bisect_left, bisect_right
from typing import List


# @leet start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        # for every house, find the closest heater via bsearch

        inf = 10**10
        n = len(heaters)
        ans = 0
        for h in houses:
            i = bisect_right(heaters, h)
            j = bisect_left(heaters, h)

            lte = heaters[i - 1] if i > 0 else None
            gte = heaters[j] if j < n else None

            left_diff = h - lte if lte is not None else inf
            right_diff = gte - h if gte is not None else inf

            radius = min(left_diff, right_diff)
            ans = max(ans, radius)
        return ans


# @leet end

houses = [1, 2, 3]
heaters = [2]
x = Solution().findRadius(houses, heaters)
print(x)

[1, 2, 3, 4]
[1, 4]

[1, 5]
[2]

