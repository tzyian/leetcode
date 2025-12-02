# @leet imports start
from typing import List, Optional

# @leet imports end
from functools import cache


# @leet start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # iterate through all possible sums of combinations of + and -
        dp = set()
        dp.add(0)
        for wt in stones:
            new_dp = set()
            for st in dp:
                # for every existing sum,
                # include sum+wt and sum-wt
                new_dp.add(st + wt)
                new_dp.add(st - wt)
            dp = new_dp
        return min(abs(i) for i in dp)


# @leet end
class SolutionExp:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)

        @cache
        def helper(i: int, tot: int) -> int:
            # find the partition where the diff between the two sets are minimal
            if i >= n:
                return tot

            take = helper(i + 1, tot + stones[i])
            notake = helper(i + 1, tot - stones[i])
            return min(abs(take), abs(notake))

        return helper(0, 0)


s = [2, 7, 4, 1, 8, 1]
x = Solution().lastStoneWeightII(s)
print(x)


s = [31, 26, 33, 21, 40]
x = Solution().lastStoneWeightII(s)
print(x)

