# 518. Coin Change II is unordered (combinations)
## loop over coins first to prevent double counting
# combinationSum4 is ordered (permutations)
## loop over numbers first to allow double counting


# if there are -ve numbers,
# there needs to be a restriction on number of uses for each number

from typing import List


# @leet start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i - x]

        return dp[target]
