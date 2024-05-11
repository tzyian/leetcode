// https://leetcode.com/problems/coin-change

from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1

        n = len(coins)

        @cache
        def dp(index, remaining) -> int:
            if remaining == 0:
                return 0
            if index == n:
               return math.inf

            ans = dp(index + 1, remaining) #skip
            if remaining >= coins[index]: # take
                ans = min(ans, 1 + dp(index, remaining - coins[index]))
            return ans


        x = dp(0, amount)

        if x > 2<<32:
            return -1
        return x






