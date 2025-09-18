from typing import List


# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy at lowest price
        # sell at highest price
        # take 0 to i as the best result after selling everything
        # at time i, you can buy exactly once, and sell at time i-1.
        #       or not buy at all
        # at time j, you take the best result at time i,
        #       then consider i + 1 to j

        dp = dict()
        n = len(prices)

        def dfs(i: int, canBuy: bool) -> int:
            nonlocal dp

            if i >= n:
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, canBuy)] = max(sell, cooldown)

            return dp[(i, canBuy)]

        return dfs(0, True)


# @leet end
