from collections import Counter
from typing import List


# @leet start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # O(n) TC for enumeration
        # O(n) SC for Counter

        # i < j,
        # j - i != nums[j] - nums[i]
        # j - nums[j] != i - nums[i]

        n = len(nums)
        total_pairs = n * (n - 1) // 2

        ctr = Counter()
        good_pairs = 0
        for i in range(n):
            res = nums[i] - i
            good_pairs += ctr[res]
            ctr[res] += 1

        return total_pairs - good_pairs


# @leet end
