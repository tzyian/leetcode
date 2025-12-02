from typing import List


# @leet start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)

        if tot & 1 == 1:
            return False

        half = tot // 2

        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for j in range(half, num - 1, -1):
                # dp[j] |= dp[j - num]
                if dp[j - num]:
                    dp[j] = True
                if dp[half]:
                    return True
        return dp[half]


# @leet end
