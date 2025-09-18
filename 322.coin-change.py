from typing import List


# @leet start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        inf = 1_000_000
        # dp representing number of coins to reach here
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        if dp[amount] != inf:
            return dp[amount]
        else:
            return -1


# @leet end

