# @leet imports start
from bisect import bisect_left, bisect_right
from collections import deque
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # we always want to empty the flooded pond that will be next flooded
        # 0 4 1 2 0 2 0 1 3
        # empty 2, 1, but not 3 or 4

        n = len(rains)
        ans = [1] * n
        last_rained = dict()
        for i, d in enumerate(rains):
            if d == 0:
                continue

            if d in last_rained:
                for j in range(last_rained[d], i):
                    if rains[j] == 0:
                        rains[j] = -1
                        ans[j] = d
                        break
                else:
                    return []
                rains[i] = -1

            last_rained[d] = i
            ans[i] = -1

        return ans


# @leet end


r = [0, 4, 1, 2, 0, 2, 0, 1, 3]
x = Solution().avoidFlood(r)
print(x)
