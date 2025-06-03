from collections import Counter
from heapq import heappop, heappush
from typing import List

"""
5 * 5
1 * 3
6 * 2

"""


# @leet start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for e in nums:
            if e < k:
                return -1

        MAX_NUM = 100
        ctr = [0] * (MAX_NUM + 1)
        for e in nums:
            ctr[e] += 1

        running = 0
        for i in range(MAX_NUM, k, -1):
            if ctr[i] > 0:
                running += 1
        return running


# @leet end

t1 = [5, 2, 5, 4, 5]
f = lambda a, b: Solution().minOperations(a, b)
x = f(t1, 2)
print(x)

# t2 = [2,1,2]
# f(t2, 2)
#
# t3 = [9,7,5,3]
# f(t3, 1)
#
#

