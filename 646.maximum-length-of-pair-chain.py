# @leet imports start
from typing import List, Optional

# @leet imports end

from bisect import bisect_left


# @leet start
class Solution:
    # NOTE: PATIENCE DOES NOT WORK
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Patience
        # [a, b], [c, d] if b < c
        pairs.sort()
        dp: List[int] = []  # list of d
        ans = 1
        for pair in pairs:
            c, d = pair

            if dp and dp[-1] < c:
                dp.append(d)
                ans = max(ans, len(dp))
            else:
                i = bisect_left(dp, c)
                dp[i] = c
                ans = max(ans, i + 1)
        print(dp)
        return ans


# @leet end


class SolutionNaive:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # [a, b], [c, d] if b < c

        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        ans = 1
        for i in range(n):
            c, d = pairs[i]
            for j in range(i):
                a, b = pairs[j]
                if b < c:
                    dp[i] = max(dp[i], 1 + dp[j])
                    ans = max(dp[i], ans)

        return ans


p = [[1, 2], [2, 3], [3, 4]]
x = Solution().findLongestChain(p)
print(x)

[[1, 2], [7, 8], [4, 5]]

