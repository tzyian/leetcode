# @leet imports start
from typing import List

# @leet imports end


# @leet start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold = -(10**10)
        nohold = 0

        for i in range(n):
            temp = hold
            hold = max(nohold - prices[i] - fee, hold)
            nohold = max(temp + prices[i], nohold)

        return nohold


# @leet end

p = [10,80,20,40,30,50,40,60,50,70,60,10,200]
f = 30
