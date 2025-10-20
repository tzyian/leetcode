# @leet imports start
from typing import *

# @leet imports end
from bisect import bisect_left

"""
Sorting by width,
every next envelope is guaranteed to be bigger or equal than before
so no need to care about width anymore

Key idea is to sort by height descending
This allows only need to care about same width but smaller height
Env = (2,6),(3,9),(3,8)
9 is included, then replaced by 8,
LIS = [6, 8]
next items: (5,5)
LIS = [5, 8] 
Then (5,5) is a new pile of only length 1

Note the patience LIS algo just overlays all LIS on top of each other
Hence you can replace inside the LIS array
In the 2d case, it's the same
"""


# @leet start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for w, h in envelopes:
            if not lis or h > lis[-1]:
                lis.append(h)
            else:
                idx = bisect_left(lis, h)
                ### idx will never == len because we append it above
                # if idx == len(lis):
                #     continue
                lis[idx] = h

        return len(lis)

    def maxEnvelopesDp(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n

        ans = 1
        for i in range(n):
            h1, w1 = envelopes[i]
            for j in range(i):
                h2, w2 = envelopes[j]
                if h2 < h1 and w2 < w1:
                    dp[i] = max(dp[i], 1 + dp[j])
                    ans = max(ans, dp[i])

        return ans


# @leet end

envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
x = Solution().maxEnvelopes(envelopes)
print(x)
print("===" * 10)


envelopes = [
    [10, 4],
    [13, 18],
    [1, 5],
    [13, 15],
    [3, 12],
    [12, 11],
    [17, 15],
    [7, 1],
    [17, 18],
    [7, 19],
    [2, 5],
    [8, 9],
    [18, 10],
    [7, 6],
    [17, 7],
]
x = Solution().maxEnvelopes(envelopes)
print(x)  # 6

