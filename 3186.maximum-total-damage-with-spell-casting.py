# @leet imports start
from typing import List, Optional

# @leet imports end

# Similar to House Robber and Delete and Earn

from collections import Counter


# @leet start
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)

        spells = [0, 0, 0] + sorted(c.keys())
        n = len(spells)
        dp = [0] * n

        for i in range(3, n):
            to_add = spells[i] * c[spells[i]]
            if spells[i] - spells[i - 1] > 2:
                # just take the last spell
                dp[i] = dp[i - 1] + to_add
            elif spells[i] - spells[i - 2] > 2:
                # we have to avoid the previous spell
                dp[i] = max(dp[i - 1], dp[i - 2] + to_add)
            else:
                # this is dp, so we only need to check dp[i-1]
                dp[i] = max(dp[i - 1], dp[i - 3] + to_add)
        return dp[-1]


# @leet end


class SolutionTLE:
    def maximumTotalDamage(self, power: List[int]) -> int:
        highest = max(power)

        c = Counter(power)

        before = 0
        prev = 0
        curr = 0
        for v in range(highest + 1):
            temp = before
            before = prev
            prev = curr
            curr = max(prev, temp + c[v] * v)

        return curr


x = [1, 1, 3, 4]
x = Solution().maximumTotalDamage(x)
print(x)

x = [7, 1, 6, 6]
x = Solution().maximumTotalDamage(x)
print(x)
