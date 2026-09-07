# @leet imports start
from typing import List, Optional

# @leet imports end

# this is quite similar to 518. Coin Change II


# @leet start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = number of ways to form first i characters of t
        # using the first j characters of s

        n = len(t)  # i
        m = len(s)  # j
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 1 way to form i=0 chars using first j characters
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # character equals
                if t[i - 1] == s[j - 1]:
                    take = dp[i - 1][j - 1]
                    notake = dp[i][j - 1]
                    dp[i][j] = take + notake
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]


# @leet end

s = "rabbbit"
t = "rabbit"
x = Solution().numDistinct(s, t)
print(x)

