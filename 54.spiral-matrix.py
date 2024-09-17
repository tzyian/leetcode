# @leet start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = 0
        last_row = rows - 1
        first_col = 0
        last_col = cols - 1

        ans = []

        while True:
            for i in range(first_col, last_col + 1):
                ans.append(matrix[first_row][i])
            first_row += 1

            if len(ans) == rows * cols:
                break

            for j in range(first_row, last_row + 1):
                ans.append(matrix[j][last_col])
            last_col -= 1

            if len(ans) == rows * cols:
                break

            for k in range(last_col, first_col - 1, -1):
                ans.append(matrix[last_row][k])
            last_row -= 1

            if len(ans) == rows * cols:
                break

            for h in range(last_row, first_row - 1, -1):
                ans.append(matrix[h][first_col])
            first_col += 1

            if len(ans) == rows * cols:
                break

        return ans


# @leet end

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1]]
m3 = [[1, 2], [3, 4]]
m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
x = Solution().spiralOrder(m4)
print(x)
