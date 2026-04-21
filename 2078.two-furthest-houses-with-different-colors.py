# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        best = 0
        n = len(colors)
        l = 0
        r = n - 1
        while l < r:
            if colors[l] != colors[r]:
                best = r - l
                break
            else:
                l += 1

        l = 0
        r = n - 1
        while l < r:
            if colors[l] != colors[r]:
                best = max(best, r - l)
                break
            else:
                r -= 1

        return best


# @leet end

