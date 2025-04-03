from typing import List


# @leet start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        diff = 0
        best = 0
        highest = 0
        for ele in nums:
            best = max(diff * ele, best)
            diff = max(diff, highest - ele)
            highest = max(highest, ele)

        return best


# @leet end

