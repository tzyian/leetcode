from collections import Counter
from typing import List


# @leet start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # O(n^2) time,
        # O(n) space
        n = len(nums)
        ctr = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                ctr[prod] += 1

        ans = 0
        for v in ctr.values():
            # *4 because
            # a,b and b,a are diff
            # and likewise for c,d and d,c
            # nP2 = n(n-1)
            ans += 4 * v * (v - 1)

        return ans


# @leet end

