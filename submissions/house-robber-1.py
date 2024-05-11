// https://leetcode.com/problems/house-robber

from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dp(prev: bool, i: int) -> int:
            if i == len(nums):
                return 0

            ans = dp(False, i + 1)

            if not prev:            
                take = nums[i] + dp(True, i + 1)
                ans = max(ans, take)
            return ans
        
        return dp(False, 0)
