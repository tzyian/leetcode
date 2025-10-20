# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        diffs = sorted(c - r for c, r in zip(capacity, rocks))
        ans = 0
        for d in diffs:
            if d > additionalRocks:
                break
            ans += 1
            additionalRocks -= d
        return ans


# @leet end

