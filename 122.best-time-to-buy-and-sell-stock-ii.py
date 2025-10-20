# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # actually greedy works here.

        # Case 1
        # If a seq incerases e.g. [1,5,100]
        # then 1 -> 100 is the same as buying and selling
        # every time there is increase,
        # because waiting is same as splitting profis

        # Case 2
        # [1,5,4,100]
        # If it drops in between, waiting is worse or equal
        # 99 vs 100

        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

    def maxProfitDp(self, prices: List[int]) -> int:
        # state machine solution
        n = len(prices)
        hold = -prices[0]
        nothold = 0
        for i in range(1, n):
            temp = nothold
            nothold = max(nothold, prices[i] + hold)
            hold = max(hold, temp - prices[i])

        return nothold


# @leet end

p = [7, 1, 5, 3, 6, 4]
x = Solution().maxProfit(p)
print(x)

[1, 2, 3, 4, 5]

[7, 6, 4, 3, 1]

