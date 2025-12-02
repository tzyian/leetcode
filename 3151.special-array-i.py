# @leet start
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if ((nums[i] & 1) ^ (nums[i - 1] & 1)) == 0:
                return False
        return True


# @leet end
