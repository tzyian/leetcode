# @leet start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # just use current_streak is easier
        highest = nums[0]
        best_length = 1
        start = 0

        for i in range(1, len(nums)):
            ele = nums[i]
            if ele > highest:
                highest = ele
                start = i
                best_length = 1
            elif ele == highest and nums[i - 1] != highest:
                start = i
            elif ele == highest:
                best_length = max(best_length, i - start + 1)
            else:  # ele < highest
                start = i

        return best_length

    def longestSubarrayNaive(self, nums: List[int]) -> int:
        best_length = 1
        start = 0
        highest = nums[0]
        prev = nums[0]

        for i, ele in enumerate(nums):
            if (ele & prev) >= highest and ele <= highest:
                # extending the subarray is better
                highest = ele & prev
                prev = highest
                best_length = max(best_length, i - start + 1)
            elif ele > highest:
                # start the count from here
                start = i
                prev = ele
                best_length = 1
                highest = ele
            else:
                # restart the count
                start = i
                prev = ele

        return best_length


# @leet end
