from typing import List


# @leet start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[0][j] = dp[0][j - 1]
                elif j == 0:
                    dp[i][0] = dp[i - 1][j]

                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[n - 1][m - 1]


# @leet end

g = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
g = [[0, 1]]
x = Solution().uniquePathsWithObstacles(g)
print(x)

