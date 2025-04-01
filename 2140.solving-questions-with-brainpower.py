from functools import cache
from typing import List


# @leet start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def helper(curr: int) -> int:
            if curr >= n:
                return 0
            pts, bpow = questions[curr]
            take = pts + helper(curr + bpow + 1)
            notake = helper(curr + 1)
            return max(take, notake)

        return helper(0)


# @leet end

