// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

from functools import cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        free = 0
        hold = -prices[0]
        
        for i in range(1, n):
            tmp = hold # cost of holding this item
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        return free

        '''
        free = [0] * n
        hold = [0] * n
        free[0] = 0
        hold[0] = -prices[0]
        for i in range(1, n): # note it is 1, n
            free[i] = max(free[i - 1], 
                          hold[i - 1] + prices[i] - fee
                         )
            hold[i] = max(hold[i - 1], 
                          free[i - 1] - prices[i]
                         )
        return free[-1]
        '''


        ''' #Memory limit exceeded
        @cache
        def dp(bought_at: int, held: bool, index: int) -> int:
            # 2 base cases
            if held and index == n - 1:
                return prices[index] - bought_at - fee
            elif not held and index == n -1:
                return 0

            
            # if not holding, can buy or no_buy
            # if holding, can sell or no_sell
            

            if not held:
                buy = dp(prices[index], True, index + 1)
                no_buy = dp(0, False, index + 1)
                return max(buy, no_buy)
            elif held:
                sell = prices[index] - bought_at - fee + dp(0, False, index + 1)
                no_sell = dp(bought_at, True, index + 1)
                return max(sell, no_sell)
        
        return dp(0, False, 0)
        '''

        