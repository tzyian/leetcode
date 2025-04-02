from typing import List


# @leet start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # O(n) TC,
        # O(1) SC
        n = len(nums)
        best = 0
        diff = 0
        highest = 0
        # elements are all non-negative
        for ele in nums:
            best = max(ele * diff, best)
            diff = max(diff, highest - ele)
            highest = max(highest, ele)

        return best


# @leet end
