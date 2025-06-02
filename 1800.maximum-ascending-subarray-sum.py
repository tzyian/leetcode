from typing import List


# @leet start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = nums[0]
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr += nums[i]
                best = max(curr, best)
            else:
                curr = nums[i]
        return best
        
        
# @leet end
