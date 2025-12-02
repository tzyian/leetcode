# @leet imports start
from typing import List, Optional

# @leet imports end


# @leet start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        inf = 10**9 + 7

        mod1_s = inf
        mod1_l = inf
        mod2_s = inf
        mod2_l = inf
        div3 = 0

        tot = 0
        for x in nums:
            tot += x

            k = x % 3
            if k == 0:
                div3 += x
            elif k == 1:
                if x < mod1_l:
                    if x < mod1_s:
                        mod1_l = mod1_s
                        mod1_s = x
                    else:
                        mod1_l = x
            elif k == 2:
                if x < mod2_l:
                    if x < mod2_s:
                        mod2_l = mod2_s
                        mod2_s = x
                    else:
                        mod2_l = x

        rem = tot % 3
        if rem == 0:
            return tot
        elif rem == 1:
            # remove a num of rem 1 or 2 numbers of rem 2
            return max(div3, tot - mod1_s, tot - mod2_s - mod2_l)
        else:
            # remove a num of rem 2 or 2 numbers of rem 1
            return max(div3, tot - mod2_s, tot - mod1_s - mod1_l)


# @leet end

nums = [3, 6, 5, 1, 8]
x = Solution().maxSumDivThree(nums)
print(x)

