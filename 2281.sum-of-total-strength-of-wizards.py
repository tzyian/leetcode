# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        nums = strength
        MOD = 10**9 + 7

        psums = [0]
        for num in nums:
            psums.append(num + psums[-1])

        weakest_i = 0
        weaks = []
        for i, x in enumerate(nums):
            if x < nums[weakest_i]:
                weakest_i = i
            weaks.append(weakest_i)

        # mins = []  # the weakest wizard up to index i
        # stack = []  # monotonically decreasing
        # for i, x in enumerate(nums):
        #     while stack and nums[stack[-1]] > x:
        #         stack.pop()
        #     stack.append(i)
        #     mins.append(i)

        print(psums)
        print(weaks)

        ans = 0
        return ans % MOD


# @leet end


s = [5, 2, 3, 5, 4, 1, 2]
x = Solution().totalStrength(s)
print(x)

