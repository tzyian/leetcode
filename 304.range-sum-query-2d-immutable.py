from typing import List


# @leet start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        psum = [[0] * m for _ in range(n)]

        psum[0][0] = matrix[0][0]
        # left col
        for i in range(1, n):
            psum[i][0] = matrix[i][0] + psum[i - 1][0]
        # top row
        for j in range(1, m):
            psum[0][j] = matrix[0][j] + psum[0][j - 1]
        # rest
        for i in range(1, n):
            for j in range(1, m):
                psum[i][j] = (
                    matrix[i][j] + psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1]
                )
        self.psum = psum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        psum = self.psum
        cgt0 = col1 - 1 >= 0
        rgt0 = row1 - 1 >= 0
        bgt0 = cgt0 and rgt0

        abcd = psum[row2][col2]
        a = psum[row1 - 1][col1 - 1] if bgt0 else 0
        ab = psum[row1 - 1][col2] if rgt0 else 0
        ad = psum[row2][col1 - 1] if cgt0 else 0

        # ABCD - AB - AD + A
        # A B
        # D C
        return abcd - ab - ad + a


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @leet end
