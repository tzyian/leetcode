# @leet imports start
from typing import *

# @leet imports end


# @leet start
from functools import cache


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        NOT_HOLDING = 0
        HOLDING = 1
        SHORT_SELL = 2

        @cache
        def dp(i: int, k_left: int, state: int) -> int:
            if i == n or k_left == 0:
                if state == NOT_HOLDING:
                    return 0
                else:
                    return -(10**10)
            if state == NOT_HOLDING:
                buy = -prices[i] + dp(i + 1, k_left, HOLDING)
                skip = dp(i + 1, k_left, NOT_HOLDING)
                short = prices[i] + dp(i + 1, k_left, SHORT_SELL)
                return max(buy, skip, short)
            elif state == HOLDING:
                sell = prices[i] + dp(i + 1, k_left - 1, NOT_HOLDING)
                skip = dp(i + 1, k_left, HOLDING)
                return max(sell, skip)
            else:  # SHORT_SELL
                buy_back = -prices[i] + dp(i + 1, k_left - 1, NOT_HOLDING)
                skip = dp(i + 1, k_left, SHORT_SELL)
                return max(buy_back, skip)

        return dp(0, k, NOT_HOLDING)


# @leet end

p = [1, 7, 9, 8, 2]
k = 2
x = Solution().maximumProfit(p, k)
print(x)

[12, 16, 19, 19, 8, 1, 19, 13, 9]
3
