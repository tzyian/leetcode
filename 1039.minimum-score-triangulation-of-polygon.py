# @leet imports start
from functools import cache
from typing import List

# @leet imports end


# @leet start
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # dp[i][j] means TRI[start_i, end_j], both inclusive, with k within
        # dp[i][j] needs to be initialised to 0 since 0 is a valid result

        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # the trick is to move i backwards
        # and you move j before k
        # so dp[i][j] is already computed when you need it
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    tri = values[i] * values[k] * values[j]
                    if dp[i][j] == 0:  # this branch is the other tricky part
                        dp[i][j] = tri + dp[i][k] + dp[k][j]
                    else:
                        dp[i][j] = min(dp[i][j], tri + dp[i][k] + dp[k][j])

        return dp[0][n - 1]


# @leet end
class SolutionRec:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        inf = 10**10

        @cache
        def dp(i: int, j: int) -> int:
            if i + 2 > j:
                return 0
            if i + 2 == j:
                tri = values[i] * values[i + 1] * values[i + 2]
                return tri

            ans = inf
            for k in range(i + 1, j):
                # select a triangle with vertices i k j,
                # the edges don't have to be coincident with the polygon edges
                tri = values[i] * values[k] * values[j]
                subs = tri + dp(i, k) + dp(k, j)
                ans = min(ans, subs)
            return ans

        return dp(0, n - 1)
