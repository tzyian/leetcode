from typing import List

# @leet start
"""
a ^ a = 0
0 ^ a = a
"""


class Solution:
    # O(2^n) TC, O(n) recursion
    # same as 78. Subsets

    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        self.ans = 0
        self.subset = 0

        def backtrack(i: int) -> None:
            self.ans += self.subset

            for i in range(i, n):
                # xor
                self.subset ^= nums[i]
                backtrack(i + 1)
                # undo xor
                self.subset ^= nums[i]

        backtrack(0)
        return self.ans


# @leet end
