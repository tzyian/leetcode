# @leet start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = nums[0]
        psum = 0

        for ele in nums:
            psum = max(ele, psum + ele)
            best = max(best, psum)

        return best


# @leet end
