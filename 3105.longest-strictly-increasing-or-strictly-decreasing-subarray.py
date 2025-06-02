from typing import List


# @leet start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        tot = 1
        ci = 1
        cd = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                ci += 1
                tot = max(tot, ci)
            else:
                ci = 1
            if nums[i] > nums[i-1]:
                cd += 1
                tot = max(tot, cd)
            else:
                cd = 1
            

        return tot
        
# @leet end
