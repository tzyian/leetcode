from typing import List


# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest = prices[0]
        n = len(prices)

        for i in range(n):
            ans = max(ans, prices[i] - lowest)
            lowest = min(lowest, prices[i])

        return ans


# @leet end
