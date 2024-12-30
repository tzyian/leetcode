# @leet start
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numst = tuple(nums)
        return self.helper(numst, target, 0)

    @cache
    def helper(self, nums: tuple[int, ...], target: int, idx: int) -> int:
        if idx == len(nums):
            return 1 if target == 0 else 0
        add = self.helper(nums, target - nums[idx], idx + 1)
        sub = self.helper(nums, target + nums[idx], idx + 1)
        return add + sub


# @leet end

