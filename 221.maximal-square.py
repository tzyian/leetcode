# @leet imports start
from typing import *

# @leet imports end


# @leet start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        1 1 0
        1 1 0
        0 0 0

        dp[i][j] means the largest size of the square towards the top left corner
        """
        n = len(matrix)
        m = len(matrix[0])
        mat = [[True if cell == "1" else False for cell in row] for row in matrix]

        dp = [[0] * m for _ in range(n)]
        ans = 0
        for i in range(n):
            if mat[i][0] == 1:
                dp[i][0] = 1
                ans = 1
        for j in range(m):
            if mat[0][j] == 1:
                dp[0][j] = 1
                ans = 1

        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    continue
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )
                ans = max(ans, dp[i][j] ** 2)

        return ans


# @leet end

m = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
x = Solution().maximalSquare(m)
print(x)

m = [["0", "1"], ["1", "0"]]
x = Solution().maximalSquare(m)
print(x)

