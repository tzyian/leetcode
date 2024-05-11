// https://leetcode.com/problems/minimum-cost-to-cut-a-stick

'''
recurrence relation: 
dp[i][j] = min(
    dp[i, a] + d[a + 1, j] + C[j-i],
    dp[i, b] + d[b + 1, j] + C[j-i]
    )

if [i]==[j] dp[i][j] = 0
'''

from sortedcontainers import SortedSet
from functools import cache
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cutset = SortedSet(cuts)
        # print(len(cutset))

        @cache
        def dp(start, stop):
            if start >= stop or start + 1 == stop or higher(start) >= stop: # if the next cut comes after stop, no need to cut
                return 0
            minimise = 1000000000
            for i in cutset[floorkey(start):ceilingkey(stop)]:
                minimise = min(minimise, dp(start, i) + dp(i, stop) + stop - start)
            # if minimise == 1000000: 
            #     print(start, stop, higher(start))
            return minimise
        
        @cache
        def higher(val): # find the value of cutset strictly higher than val
            n = len(cutset)
            if cutset[n - 1] < val or cutset.bisect_right(val) >= len(cutset):
                return 10000000
            return cutset[cutset.bisect_right(val)]
        
        @cache 
        def floorkey(val): # find the index of cutset that is <= val
            if val in cutset:
                return cutset.bisect_left(val) + 1
            return cutset.bisect_left(val)

        @cache 
        def ceilingkey(val): # find the index of cutset that is >= val
            if val in cutset:
                return cutset.bisect_right(val) - 1
            return cutset.bisect_right(val)
        
        return dp(0, n)


    

