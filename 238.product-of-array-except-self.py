from typing import List


# @leet start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) TC, O(n) SC
        psum = 1
        ssum = 1
        prods = []
        n = len(nums)
        for i in range(n):
            prods.append(psum)
            psum *= nums[i]

        for i in reversed(range(n)):
            prods[i] *= ssum
            ssum *= nums[i]

        return prods


# @leet end
