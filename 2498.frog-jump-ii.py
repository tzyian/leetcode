# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # this is a greedy odd and even problem
        n = len(stones)

        if n == 2:
            return stones[1] - stones[0]

        longest = 0
        i = 3
        j = 2
        while i < n:
            diff = stones[i] - stones[i - 2]
            longest = max(longest, diff)
            i += 2

        while j < n:
            diff = stones[j] - stones[j - 2]
            longest = max(longest, diff)
            j += 2

        return longest


# @leet end

