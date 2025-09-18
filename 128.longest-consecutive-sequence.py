from collections import Counter
from typing import List


# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        c = set(nums)
        starts = set()
        for e in c:
            if e - 1 not in c:
                starts.add(e)

        for i in starts:
            chain = 0
            while i in c:
                i += 1
                chain += 1
            ans = max(chain, ans)

        return ans


# @leet end

